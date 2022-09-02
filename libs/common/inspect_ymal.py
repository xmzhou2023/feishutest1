import logging
import os
import sys

import yaml
from libs.common.time_ui import timestamp
from libs.config.conf import PEROJECT_PATH, LOCATE_MODE


def get_FolderName(filepath):
    pro_list = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s' % (allDir))
        pro_list.append(child)
    return pro_list


def inspect_element():
    """审查所有的元素是否正确"""
    print("【开始】请稍候，元素定位库文件自检程序开始！")
    start_time = timestamp()
    pro_list = get_FolderName(PEROJECT_PATH)

    error_list = []
    for pro in pro_list:
        ELEMENT_PATH = os.path.join(PEROJECT_PATH, pro, 'page_element')
        for i in os.listdir(ELEMENT_PATH):
            _path = os.path.join(ELEMENT_PATH, i)
            if os.path.isfile(_path):
                with open(_path, encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                    try:
                        if data is None:
                            error_list.append('【项目】%s【模块】%s中元素格式不符' % (pro, i))

                        if isinstance(data, dict) is False:
                            error_list.append(
                                '【项目】%s【模块】%s请检查元素名和表达式固定格式【元素定位名: 定位方式==定位路径】' % (pro, i))

                        for k,v in data.items():

                            if k is None:
                                error_list.append('【项目】%s【模块】%s【元素】%s【定位表达式】%s定位方式和值未填写' % (pro, i, k, v))

                            if '==' not in k:
                                error_list.append('【项目】%s【模块】%s【元素】%s【定位表达式】%s标签和路径需用==间隔' % (pro, i, k, v))

                            pattern, value = k.split('==')

                            if pattern not in LOCATE_MODE:
                                error_list.append('【项目】%s【模块】%s【元素】%s【定位表达式】%s没有指定类型' % (pro, i, k, v))

                            if pattern in ('id', 'name', 'css', 'class', 'text', 'partial-link', 'tag'):
                                continue

                            if pattern == 'xpath':
                                if '/' not in value:
                                    error_list.append('【项目】%s【模块】%s【元素】%s【定位表达式】%sxpath类型与值不配！' % (pro, i, k, v))

                                if '“' in value or '‘' in value:
                                    error_list.append('【项目】%s【模块】%s【元素】%s【定位表达式】%s注意不要用中文符号的引号！' % (pro, i, k, v))

                            # if pattern == 'css':
                            #     if '/' not in value:
                            #         print('【提示】【%s】项目【%s】模块【%s】元素css类型与值不配' % (pro, i, k))
                            #         error_list += 1

                            # if pattern == 'id':
                            #     if '/' not in value:
                            #         print('【提示】【%s】项目【%s】模块【%s】元素css类型与值不配' % (pro, i, k))
                            #         error_list += 1
                    except:
                        continue

    end_time = timestamp()
    print("【结束】恭喜您，元素库文件自检程序完成！用时%.3f秒！" % (end_time - start_time))
    if len(error_list) != 0:
        raise AttributeError('\n%s\n【提示】请尽快检查并修改自己的用例，如有异议，请尽快联系我们，谢谢！' % error_list)


if __name__ == '__main__':
    # print(get_FolderName(PEROJECT_PATH))
    inspect_element()
