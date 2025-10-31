from nicegui import ui
import qrcode
import io
import base64
import socket
import webbrowser

# --- 辅助函数：获取本机的局域网 IP ---
def get_host_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # 连接一个外部地址 (不发送数据，只是为了获取正确的网卡IP)
        s.connect(('10.255.255.255', 1))
        host_ip = s.getsockname()[0]
    except Exception:
        host_ip = '127.0.0.1' # 如果没有网络连接，则回退到 localhost
    finally:
        s.close()
    return host_ip

# --- 定义您的应用端口 ---
APP_PORT = 8080

# ---------- 首页 ----------
@ui.page('/')
def main_page():
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-gradient-to-b from-blue-50 to-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200 relative'):
        # 状态栏
        with ui.row().classes('justify-between items-center px-4 pt-3 text-gray-500 text-sm'):
            ui.label('9:41')
            ui.label('- 模拟X300卖点交互页 - 周天宇 -')
            ui.label('📶 100% 🔋')

        # ... (您的其他卖点代码 ...）
        # 卖点1：蔡司两亿超级主摄
        with ui.card().classes('m-3 p-4 cursor-pointer hover:shadow-lg transition-all rounded-2xl'):
            ui.label('如果，你也觉得出门背相机太麻烦……').classes('text-lg font-semibold mt-3 text-gray-800')      
            ui.image('200mp.jpg').classes('rounded-xl')
            ui.label('蔡司2亿超级主摄').classes('w-full text-center text-lg font-semibold mt-3 text-gray-800')
            ui.label('2亿人像超清晰，旅拍何必带相机。高清镜头下的你，美得自然而然。').classes('text-sm text-gray-600 mt-1')
            ui.button('立即体验', on_click=lambda: ui.navigate.to('/1')).classes('mt-3 w-full bg-blue-500 text-white rounded-lg')

        # 卖点2：全焦段高清人像
        with ui.card().classes(
            'my-3 p-4 rounded-2xl hover:shadow-lg transition-all w-full box-border overflow-visible').style('height: auto; min-height: 420px;'):
            ui.label('全焦段高清人像').classes('w-full text-center text-lg font-semibold mt-3 text-gray-800')
            ui.label('23mm焦段支持2亿超高像素，5大黄金焦段支持5000万像素人像全焦段，远近都可高清出片。').classes('text-sm text-gray-600 mt-1')
            ui.label('23mm - 35mm - 50mm - 85mm - 100mm').classes('text-sm font-semibold text-gray-600 mt-1 w-full text-center')
            with ui.carousel(animated=True, arrows=True).props('infinite').style('width: 100%; height: 100%'):
                with ui.carousel_slide().classes('flex justify-center items-center'):
                    ui.image('23mm.jpg').classes('rounded-xl shadow-md')
                with ui.carousel_slide().classes('flex justify-center items-center'):
                    ui.image('35mm.jpg').classes('rounded-xl shadow-md')
                with ui.carousel_slide().classes('flex justify-center items-center'):
                    ui.image('50mm.jpg').classes('rounded-xl shadow-md')
                with ui.carousel_slide().classes('flex justify-center items-center'):
                    ui.image('85mm.jpg').classes('rounded-xl shadow-md')
                with ui.carousel_slide().classes('flex justify-center items-center'):
                    ui.image('100mm.jpg').classes('rounded-xl shadow-md')
            ui.button('本地样张', on_click=lambda: ui.navigate.to('/2')).classes('mt-3 w-full bg-blue-500 text-white rounded-lg')


        # 卖点3：Live图
        with ui.card().classes('m-3 p-4 cursor-pointer hover:shadow-lg transition-all rounded-2xl'):
            ui.label('如果，你喜欢用实况照片记录生活……').classes('text-lg font-semibold mt-3 text-gray-800') 
            ui.image('video.gif').props('muted loop').classes('rounded-xl')
            ui.label('Live Photo').classes('w-full text-center text-lg font-semibold mt-3 text-gray-800')
            ui.label('Live图全面优化，兼具防抖、抓拍定格等多样化能力，还支持视频转Live图，更加灵动鲜活、多巴胺爆棚的生命力，跃然眼前。').classes('text-sm text-gray-600 mt-1')
            ui.button('了解更多', on_click=lambda: ui.navigate.to('/3')).classes('mt-3 w-full bg-blue-500 text-white rounded-lg')

        # 卖点4：Vlog
        with ui.card().classes('m-3 p-4 cursor-pointer hover:shadow-lg transition-all rounded-2xl'):
            ui.label('如果，你喜欢用Vlog记录自己的旅行……').classes('text-lg font-semibold mt-3 text-gray-800') 
            ui.image('videocold.gif').props('muted').classes('rounded-xl')
            ui.label('4K 60fps冷胶人像视频').classes('w-full text-center text-lg font-semibold mt-3 text-gray-800')
            ui.label('随身Vlog神器，新增冷白、负片2种超具网感视频风格，让你的视频创作出片又出圈！').classes('text-sm text-gray-600 mt-1')
            ui.button('了解更多', on_click=lambda: ui.navigate.to('/4')).classes('mt-3 w-full bg-blue-500 text-white rounded-lg')

        # 卖点5：滤镜
        with ui.card().classes('m-3 p-4 cursor-pointer hover:shadow-lg transition-all rounded-2xl'):
            ui.label('如果，你想让旅拍更有氛围感……').classes('text-lg font-semibold mt-3 text-gray-800') 
            ui.image('packfilm.jpg').classes('rounded-xl')
            ui.label('撕拉片人像').classes('w-full text-center text-lg font-semibold mt-3 text-gray-800')
            ui.label('复古色调呈现温暖肌底，“低保真”的色彩质感带来柔和色调和朦胧感，酿造独特的时光温柔印记。').classes('text-sm text-gray-600 mt-1')
            ui.button('了解更多', on_click=lambda: ui.navigate.to('/5')).classes('mt-3 w-full bg-blue-500 text-white rounded-lg')

        # 卖点6：AI
        with ui.card().classes('m-3 p-4 cursor-pointer hover:shadow-lg transition-all rounded-2xl'):
            ui.label('又或者，你想玩点不一样的？').classes('text-lg font-semibold mt-3 text-gray-800') 
            ui.image('triptych.jpg').classes('rounded-xl')
            ui.label('AI电影分镜').classes('w-full text-center text-lg font-semibold mt-3 text-gray-800')
            ui.label('2亿超高像素，玩转单张照片二次构图、AI智能裁剪多画幅，直出胶片感电影大片，轻松出圈社交平台。').classes('text-sm text-gray-600 mt-1')
            ui.button('了解更多', on_click=lambda: ui.navigate.to('/6')).classes('mt-3 w-full bg-blue-500 text-white rounded-lg')


# ---------- 详情页 ----------
@ui.page('/1')
def night_page1(): # 注意：函数名不能重复，我帮您改了
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200'):
        ui.button('← 返回', on_click=lambda: ui.navigate.to('/')).classes('m-3 bg-gray-100 text-gray-700 rounded-xl px-4')
        ui.image('photo.jpg').classes('m-4 rounded-xl')

@ui.page('/2')
def night_page2(): # 注意：函数名不能重复
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200'):
        ui.button('← 返回', on_click=lambda: ui.navigate.to('/')).classes('m-3 bg-gray-100 text-gray-700 rounded-xl px-4')
        ui.image('sample1.jpg').classes('m-4 rounded-xl w-full h-64 object-cover')
        ui.image('sample2.jpg').classes('m-4 rounded-xl w-full h-64 object-cover')
        ui.image('sample3.jpg').classes('m-4 rounded-xl w-full h-64 object-cover')

@ui.page('/3')
def night_page3(): # 注意：函数名不能重复
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200'):
        ui.button('← 返回', on_click=lambda: ui.navigate.to('/')).classes('m-3 bg-gray-100 text-gray-700 rounded-xl px-4')
        ui.image('photo.jpg').classes('m-4 rounded-xl')

@ui.page('/4')
def night_page4(): # 注意：函数名不能重复
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200'):
        ui.button('← 返回', on_click=lambda: ui.navigate.to('/')).classes('m-3 bg-gray-100 text-gray-700 rounded-xl px-4')
        ui.image('photo.jpg').classes('m-4 rounded-xl')

@ui.page('/5')
def night_page5(): # 注意：函数名不能重复
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200'):
        ui.button('← 返回', on_click=lambda: ui.navigate.to('/')).classes('m-3 bg-gray-100 text-gray-700 rounded-xl px-4')
        ui.image('photo.jpg').classes('m-4 rounded-xl')

@ui.page('/6')
def night_page6(): # 注意：函数名不能重复
    with ui.column().classes('w-[390px] h-[844px] mx-auto bg-white rounded-[40px] shadow-2xl overflow-y-scroll border border-gray-200'):
        ui.button('← 返回', on_click=lambda: ui.navigate.to('/')).classes('m-3 bg-gray-100 text-gray-700 rounded-xl px-4')
        ui.image('photo.jpg').classes('m-4 rounded-xl')


# ---------- ⭐️ 新增：二维码显示页面 ----------
@ui.page('/qr')
def qr_page():
    with ui.column().classes('w-full h-screen flex justify-center items-center gap-4'):
        host_ip = get_host_ip()
        
        # 这个URL是二维码将指向的地址（即您的应用首页）
        access_url = f'http://{host_ip}:{APP_PORT}/' 
        
        ui.label(f'请用手机扫描二维码访问应用').classes('text-2xl font-bold')
        ui.label(f'({access_url})').classes('text-lg text-gray-500')

        # --- 生成二维码并转换为 Base64 ---
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(access_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # 保存到内存中
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        
        # 转换为 Base64 字符串 (Data URL)
        base64_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        data_url = f'data:image/png;base64,{base64_str}'
        # --- 结束 ---

        # 使用 ui.image 显示 Base64 图像
        ui.image(data_url).classes('w-64 h-64 border-4 border-gray-300')
        ui.label('确保您的手机和电脑连接在同一个 Wi-Fi 网络下').classes('text-sm text-gray-400')


# ---------- 启动应用 ----------
ui.run(host='0.0.0.0', port=APP_PORT, show=True)
# 网页后缀添加/qr