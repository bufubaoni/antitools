orange 需要安装的 东西比较多

openresty
nginx
mysql
lor

启动时报错unknown directive "lua_package_path"
此时发现
nginx 并没有指向openresty
然后联系作者指出，应将nginx连接到openresty
sudo ln -sf /usr/local/openresty/nginx/sbin/nginx /usr/sbin/nginx
执行此命令然后启动 orange 即可