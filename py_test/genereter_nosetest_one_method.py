def get_single_method(str_method):
    method, class_str = str_method.split()
    class_list = class_str.strip("()").split(".")
    class_str = class_list.pop(-1)
    file_path = "/".join(class_list)+".py"
    method_path = ".".join((class_str, method))
    return "nosetests -x -s {file_path}:{method_path}".format(file_path=file_path, method_path=method_path)


if __name__ == "__main__":
    print get_single_method("test_GetUserNotifications (service.test_report.ReactionServicerTest)")
~
