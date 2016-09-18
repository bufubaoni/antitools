import re
from collections import namedtuple
from emu_cost import emu_type

Table = namedtuple("Table", ["name", "col"])	

Column = namedtuple("Column", ["name", "type", "len"])	

package = "lms_main.Models.base.auth"
import_class = ["com.jfinal.plugin.activerecord.IBean",
                "com.jfinal.plugin.activerecord.Model"]
def getTable(table_sql):
    res_tablename = "TABLE `(.+)`"
    res_col = "`(.+)`\s([a-z]+\(.+\))\s"
    res_col_type = "(.+)\(([0-9]+)\)"
    tablename = re.findall(res_tablename, table_sql)[0]
    print(tablename)
    table = Table(tablename, list())
    cols = re.findall(res_col, table_sql)
    print(cols)
    map(lambda x: table.col.append(Column(x[0], re.findall(res_col_type, x[1])[0][0],
                                          re.findall(res_col_type, x[1])[0][1])), cols)

    return table

def generateGet(col):
    return ("public {types} get{Content}(){{ return get(\"{content}\");}}\n".format(
        types=emu_type[col.type.lower()],
        Content=col.name.title(),
        content=col.name))	

def generateSet(col):
    return (
        "public void set{Content}({types} {content}){{set(\"{content}\",{content});}}\n".format(
            types=emu_type[col.type.lower()],
            Content=col.name.title(),
            content=col.name))

def generateClass(table):
    generate = list()
    for col in table.col:
        generate.append(generateSet(col))
        generate.append(generateGet(col))
    return "public class {tablename}Model <M extends {tablename}Model<M>> extends Model<M> implements IBean {{\n{gener} }}\n".format(
        tablename=table.name,
        gener="".join(generate))
def writebaseclass(table, package):
    classname = table.name + "Model"	
    if package:
        package = package
    else:
        package = "lms_main.Models.base.auth"
    import_class = ["com.jfinal.plugin.activerecord.IBean",
                    "com.jfinal.plugin.activerecord.Model"]
	
    with open("class/{classname}.java".format(classname=classname), "w") as jclass:
        jclass.write("package {package};\n".format(package=package))
        jclass.write("\n")
        map(lambda x: jclass.write("import {import_class};\n".format(import_class=x)),
            import_class)

        jclass.write("\n")
        cla = generateClass(table)
        jclass.write(cla)
    return (package, classname)
		

def writeclass(table, package, import_class):
    classname = table.name
    main_str = "public class {name} extends {name}Model<{name}> {{public static final {name} me = new {name}();}}".format(
        name=classname,
    )
    package_list = package.split(".")
    base_index = package_list.index("base")
    package_this = ".".join(package_list[:base_index])
    with open("class/{classname}.java".format(classname=classname), "w") as jclass:
        jclass.write("package {package_this};\n".format(package_this=package_this, ))
        jclass.write("\n")
        jclass.write("import {package}.{import_class};\n".format(package=package,
                                                                 import_class=import_class, ))
        jclass.write(main_str)
        jclass.write("\n")
    print("arp.addMapping(\"{table}\",\"id\",{table}.class);".format(table=table.name))
    return (package_this, classname)
def writecontroller(table, package, import_class):
    classname = table.name + "Controller"
    main_str = (
        "public class {classname} extends Controller"
        " {{\npublic void index() {{\n}} \n}}".format(
            classname=classname))
    package_list = package.split(".")
    models_index = package_list.index("Models")
    list_pack=list(package_list[:models_index])
    list_pack.append("Controllers")
    package_this = ".".join(list_pack)
    with open("class/{classname}.java".format(classname=classname),"w") as jclass:
        jclass.write("package {package_this};\n".format(package_this=package_this, ))
        jclass.write("\n")
        jclass.write("import com.jfinal.core.Controller;")
        jclass.write("import {package}.{import_class};\n".format(package=package,
                                                                 import_class=import_class, ))
        jclass.write(main_str)
        jclass.write("\n")
    print("routes.add(\"/{tablename}\",{classname}.class);".format(classname=classname,
                                                                    tablename=table.name))
def opensql(name):
    with open("tables/{name}.sql".format(name=name), "r") as str_table:
        return "".join(str_table.readlines())
def api(name, package):
    table = getTable(opensql(name))
    (package, import_class) = writebaseclass(table, package)
    (package, import_class) = writeclass(table, package, import_class)
    writecontroller(table, package, import_class)
    print("ok")
if __name__ == "__main__":
    api("Auth_membership", "lms_main.Models.base.auth")