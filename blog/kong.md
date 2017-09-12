# kong 相关
由于业务需要，现在将kong作为负载均衡器引入项目，对项目进行多进程拆分
根据app 根url进行简单的项目拆分

## kong插件开发
根据官方文档所说，需要将插件放到usr/local/kong/plugins 即安装目录下，由于此目录没有这个文件夹需要对新建文件夹
将自己的plugin放到目录下
如
    my_plugin
    +---handler.lua
    +---schema.lua

需要符合此种最简单的文件接口

在 handler.lua 中写入
```lua
-- Extending the Base Plugin handler is optional, as there is no real
-- concept of interface in Lua, but the Base Plugin handler's methods
-- can be called from your child implementation and will print logs
-- in your `error.log` file (where all logs are printed).
local BasePlugin = require "kong.plugins.base_plugin"
local CustomHandler = BasePlugin:extend()

-- Your plugin handler's constructor. If you are extending the
-- Base Plugin handler, it's only role is to instanciate itself
-- with a name. The name is your plugin name as it will be printed in the logs.
function CustomHandler:new()
  CustomHandler.super.new(self, "my-custom-plugin")
end

function CustomHandler:init_worker(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.init_worker(self)

  -- Implement any custom logic here
end

function CustomHandler:certificate(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.certificate(self)

  -- Implement any custom logic here
end

function CustomHandler:access(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.access(self)

  -- Implement any custom logic here
end

function CustomHandler:header_filter(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.header_filter(self)

  -- Implement any custom logic here
end

function CustomHandler:body_filter(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.body_filter(self)

  -- Implement any custom logic here
end

function CustomHandler:log(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.log(self)

  -- Implement any custom logic here
end

-- This module needs to return the created table, so that Kong
-- can execute those functions.
return CustomHandler

Of course, the logic of your plugin itself can be abstracted away in another module, and called from your handler module. Many existing plugins have already chosen this pattern when their logic is verbose, but it is purely optional:

local BasePlugin = require "kong.plugins.base_plugin"

-- The actual logic is implemented in those modules
local access = require "kong.plugins.my-custom-plugin.access"
local body_filter = require "kong.plugins.my-custom-plugin.body_filter"

local CustomHandler = BasePlugin:extend()

function CustomHandler:new()
  CustomHandler.super.new(self, "my-custom-plugin")
end

function CustomHandler:access(config)
  CustomHandler.super.access(self)

  -- Execute any function from the module loaded in `access`,
  -- for example, `execute()` and passing it the plugin's configuration.
  access.execute(config)
end

function CustomHandler:body_filter(config)
  CustomHandler.super.body_filter(self)

  -- Execute any function from the module loaded in `body_filter`,
  -- for example, `execute()` and passing it the plugin's configuration.
  body_filter.execute(config)
end

return CustomHandler

```
以上为官方例子
仅仅在`access`方法中加入一个写文件的操作
```
function CustomHandler:access(config)
  -- Eventually, execute the parent implementation
  -- (will log that your plugin is entering this context)
  CustomHandler.super.access(self)
  local file = io.open("~/test_access.log","w")
  file:write("hello world!!!!")
  file:close()

  -- Implement any custom logic here
end
```
当配置这个插件后
当有请求api时会在
用户根目录下创建 `test_access.log`文件并写入*hello world!!!!*
然后插件即可正常使用

根据官方文档，plugin存放位置应该可以用户自定义，但是会根据加载习惯来添加一些内容
如
    我定义了
    lua_package_path = /usr/local/custom/?.lua
    那么kong会搜索如此的目录
    `/usr/local/custom/kong/plugins/`

高级定制功能，例如字段选择，mc之类的架构，需要再kong层做缓存