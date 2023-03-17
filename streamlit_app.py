import streamlit as st
import json

# 加载包含单位名称的 JSON 文件
with open('unit_names.json') as f:
    data = json.load(f)

# 创建 Streamlit 应用程序
st.title('单位编码查询')
unit_code = st.text_input('请输入单位编码：')

# 查询并显示单位名称
if unit_code in data['单位名称']:
    unit_name = data['单位名称'][unit_code]
    st.write(f'单位名称为：{unit_code}{unit_name}')
else:
    st.write('该单位编码不存在，请重新输入。')
