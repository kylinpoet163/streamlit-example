import streamlit as st
import json

# 加载包含单位名称的 JSON 文件
with open('unit_names.json', encoding='utf-8',errors="ignore") as f:
    data = json.load(f)
    
# 创建 Streamlit 应用程序
st.title('单位编码查询')
unit_code = st.text_input('请输入单位编码：(回车确认)')

# 查询并显示单位名称
if unit_code in data:
    unit_name = data[unit_code]
    st.write(f'单位名称为：  \n{unit_code}{unit_name}')
else:
    st.write('该单位编码不存在，请重新输入。')
