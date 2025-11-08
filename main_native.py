import flet as ft


def main(page: ft.Page):
    # 设置页面标题
    page.title = "原生Flet组件示例"

    # 设置窗口大小
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True

    # 定义主题
    def switch_theme(theme_mode):
        page.theme_mode = theme_mode
        page.update()

    # 创建一个切换主题的函数
    def toggle_theme(e):
        if page.theme_mode == "light":
            switch_theme("dark")
            toggle_button.text = "切换到浅色主题"
        else:
            switch_theme("light")
            toggle_button.text = "切换到深色主题"
        page.update()

    # 创建切换主题按钮
    toggle_button = ft.ElevatedButton(
        "切换到深色主题",
        on_click=toggle_theme
    )

    # 卡片点击事件处理函数
    def card_clicked(e):
        page.snack_bar = ft.SnackBar(content=ft.Text("卡片被点击了！"))
        page.snack_bar.open = True
        page.update()

    # 加载演示内容的函数
    def load_demo_content():
        # 清空页面
        page.controls.clear()

        # 创建所有演示内容
        demo_content = [
            # 标题文本
            ft.Text("主题色适配示例", size=32, weight=ft.FontWeight.BOLD),
            toggle_button,
            ft.Divider(),

            # 文本组件示例
            ft.Text("文本组件", size=24, weight=ft.FontWeight.W_600),
            ft.Text("这是一段正文文本"),
            ft.Text("这是一段说明文字", size=12, color=ft.Colors.GREY),
            ft.Text("带下划线的链接文本", color=ft.Colors.BLUE, weight=ft.FontWeight.W_500),
            ft.Text("不带下划线的链接文本", color=ft.Colors.BLUE),

            ft.Divider(),

            # 按钮组件示例
            ft.Text("按钮组件", size=24, weight=ft.FontWeight.W_600),
            ft.Row([
                ft.ElevatedButton("主要按钮"),
                ft.OutlinedButton("次要按钮"),
                ft.ElevatedButton("成功按钮", bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                ft.ElevatedButton("警告按钮", bgcolor=ft.Colors.ORANGE, color=ft.Colors.WHITE),
                ft.ElevatedButton("错误按钮", bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
            ]),

            ft.Divider(),

            # 输入组件示例
            ft.Text("输入组件", size=24, weight=ft.FontWeight.W_600),
            ft.Column([
                ft.TextField(label="用户名", hint_text="请输入用户名"),
                ft.Dropdown(
                    label="选择项",
                    options=[
                        ft.dropdown.Option("选项1"),
                        ft.dropdown.Option("选项2"),
                        ft.dropdown.Option("选项3"),
                    ],
                ),
                ft.Checkbox(label="同意条款"),
            ]),

            ft.Divider(),

            # 卡片组件示例
            ft.Text("卡片组件", size=24, weight=ft.FontWeight.W_600),
            ft.ResponsiveRow([
                ft.Column([
                    ft.Card(
                        content=ft.Container(
                            content=ft.Text("这是一个简单的卡片"),
                            padding=10,
                        )
                    )
                ], col={"xs": 12, "sm": 6, "md": 4}),

                ft.Column([
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("带标题的卡片", size=18, weight=ft.FontWeight.W_600),
                                ft.Text("这是卡片的内容"),
                                ft.Row([
                                    ft.ElevatedButton("确定"),
                                    ft.OutlinedButton("取消")
                                ])
                            ]),
                            padding=10,
                        )
                    )
                ], col={"xs": 12, "sm": 6, "md": 4}),

                ft.Column([
                    ft.Card(
                        content=ft.Container(
                            content=ft.Text("带边框的卡片", size=16),
                            padding=10,
                            border=ft.border.all(1, ft.Colors.GREY),
                            bgcolor=ft.Colors.TRANSPARENT,
                        ),
                        elevation=0,
                    )
                ], col={"xs": 12, "sm": 6, "md": 4}),

                ft.Column([
                    ft.Card(
                        content=ft.Container(
                            content=ft.Text("点击我！", size=20, color=ft.Colors.BLUE),
                            padding=10,
                            alignment=ft.alignment.center,
                            on_click=card_clicked,
                            ink=True,
                        )
                    )
                ], col={"xs": 12, "sm": 6, "md": 4}),

                ft.Column([
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("完整功能卡片", size=18, weight=ft.FontWeight.W_600),
                                ft.Text("这是一个展示完整功能的卡片，具有标题、内容和操作按钮。"),
                                ft.Row([
                                    ft.ElevatedButton("操作1"),
                                    ft.OutlinedButton("操作2")
                                ])
                            ]),
                            padding=10,
                        ),
                        elevation=5,
                    )
                ], col={"xs": 12, "sm": 6, "md": 4}),
            ]),

            # 添加额外的内容以确保页面可以滚动
            ft.Text("额外内容以演示滚动功能", size=24, weight=ft.FontWeight.W_600),
            ft.Text("这是额外的内容，用于演示页面滚动功能。当页面内容超出窗口大小时，用户可以滚动查看所有内容。"),

            # 添加更多卡片以增加内容高度
            *[ft.Column([
                ft.Card(
                    content=ft.Container(
                        content=ft.Text(f"额外的卡片 {i + 1}"),
                        padding=10,
                    )
                ),
                ft.Text(f"这是第 {i + 1} 个额外卡片的内容。通过添加更多内容，我们可以确保页面足够长以测试滚动功能。")
            ]) for i in range(10)]
        ]

        # 创建可滚动的内容
        scrollable_content = ft.Column(
            controls=demo_content,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.START
        )
        
        page.add(scrollable_content)
        page.scroll = ft.ScrollMode.AUTO

    # 初始加载内容
    load_demo_content()

    # 更新页面
    page.update()


ft.app(main)