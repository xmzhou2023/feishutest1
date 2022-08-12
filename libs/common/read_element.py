import os
import yaml
from libs.config.conf import PEROJECT_PATH

class Element:
    """获取元素"""
    def __init__(self, project, name):

        ELEMENT_PATH = os.path.join(PEROJECT_PATH, project, 'page_element')
        self.file_name = '%s.yaml' % name
        self.element_path = os.path.join(ELEMENT_PATH, self.file_name)
        if not os.path.exists(self.element_path):
            raise FileNotFoundError("%s 文件不存在！" % self.element_path)
        with open(self.element_path, encoding='utf-8') as f:
            self.data = yaml.safe_load(f)

    def __getitem__(self, item):
        """获取属性"""
        data = self.data.get(item)
        if data:
            name, value = data.split('==')
            return name, value
        raise ArithmeticError("{}中不存在关键字：{}".format(self.file_name, item))


if __name__ == '__main__':
    search = Element('DRP','SystemMgmt_RegionMgmt')
    print(search['tab区域菜单一级菜单'])