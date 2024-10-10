import streamlit as st
from rss import parse_rss


st.set_page_config(
    page_title="NAnime",
    page_icon="🐉",
    menu_items={
        'Get Help': 'https://TODO',
        'Report a bug': "https://TODO",
        'About': "TODO"
    }
)

st.write("""
# Welcome to NAnime!
这是部署在NJU内网的动漫下载网站。你可以通过[蜜柑计划](https://mikanani.me/)来寻找番剧对应的RSS，然后将其填入下列的表单之中。
该网站会自动对RSS进行解析，并对番剧内容进行下载。
"""
)

st.write("""
已经下载过的番剧会保留，因此**不会重复下载**已经下载过的内容。
对于下载过的番剧，你可以选择通过该网页打包下载到你的本地进行观看，
或者通过不同的播放器来连接另一个站点进行在线观看。
因为校内网的原因，你可以享受非常快的网速。
""")

st.info("请注意，同一个番剧存在多个字幕组。本网站仅下载RSS链接中**第一个出现的字幕组**的资源。另外，对于存在多个字幕的情况，本网站仅下载简体资源，忽略繁体资源。")

st.info("本网站的全部代码已经开源。不含广告，也不会存储任何用户信息")

rss_link = st.text_input("请输入动漫的 RSS 链接:")

# 当用户提交表单时显示输入结果
if st.button("提交RSS"):
    if rss_link:
        # st.success(f"你输入的 RSS 链接是: {rss_link}")
        parse_rss(rss_link)
    else:
        st.error("请输入有效的 RSS 链接")

st.write("提交后会有2种结果，如果尚未下载或者有人提交会显示**下载中**，其余时候会显示**已下载**，并给出下载链接")

st.write("你也可以直接在下面输入动漫的名字来获取下载链接（如果有的话）")

anime_name = st.text_input("请输入动漫的名字:")

# 当用户提交表单时显示输入结果
if st.button("提交动漫名称"):
    if anime_name:
        st.success(f"你输入的 RSS 链接是: {rss_link}")
    else:
        st.error("请输入有效的 RSS 链接")

if st.toggle("### 如何获取动漫 RSS"):

    st.write("#### 步骤 1: 打开[蜜柑计划](https://mikanani.me/)")
    st.write("#### 步骤 2: 查找你想下载的番剧")
    st.write("你可以通过以下几种方法来查找你想下载的番剧：")
    if st.toggle("##### 方法 1: 使用搜索框查找"):
        st.write("直接在蜜柑计划的搜索框中输入番剧的名称，进行查找并进入番剧页面。")
        st.image("images/s2.1.png", caption="使用搜索框查找番剧", use_column_width=True)

    if st.toggle("##### 方法 2: 直接在主页搜索"):
        st.write("你可以直接在主页看到当季新番，然后点击标题进入番剧页面。")
        st.image("images/s2.2.png", caption="按分类浏览番剧", use_column_width=True)


    st.write("#### 步骤 3: 获取RSS")
    st.write("在番剧详情页面中，找到并复制对应的 RSS 链接。")
    st.image("images/s3.png", caption="获取番剧的 RSS 链接", use_column_width=True)


    st.write("#### 步骤 4: 填写RSS链接")
    st.write("将上一步获取到的 RSS 链接填入上方的空格之中。")
