# -*- coding: utf-8 -*-
"""
    Author:1112
    Date:2023-09-04
    Update: ---
    Achieve:拆分大文件pdf
"""

from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_pdf, start_page, end_page):
    # 创建PdfReader对象来读取PDF文件
    pdf_reader = PdfReader(input_pdf)

    # 创建PdfWriter对象来写入拆分后的PDF文件
    pdf_writer = PdfWriter()

    # 遍历指定页码范围内的页面，并将其添加到PdfWriter对象中
    for page_num in range(start_page - 1, end_page):
        page = pdf_reader.pages[page_num]
        pdf_writer.add_page(page)

    # 将PdfWriter对象中的内容写入到输出的PDF文件中
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == '__main__':
    # 使用示例
    input_file = 'target.pdf'          # 输入的大PDF文件路径
    output_file = 'new.pdf'            # 拆分后的PDF文件路径
    start_page = "1"                   # 起始页码
    end_page = 100                     # 结束页码

    split_pdf(input_file, output_file, start_page, end_page)

