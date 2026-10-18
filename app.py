import gradio as gr
import spaces


@spaces.GPU
def greet(name):
    return f"안녕하세요, {name}님! CI/CD 배포 성공입니다."


demo = gr.Interface(
    fn=greet,
    inputs=gr.Textbox(label="이름"),
    outputs=gr.Textbox(label="결과"),
    title="CI/CD Practice"
)


if __name__ == "__main__":
    demo.launch()
