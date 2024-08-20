from flask import Flask, render_template_string
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def plot():
    # Gerar dados de exemplo para o gráfico
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    # Criar o gráfico
    plt.figure(figsize=(5, 4))
    plt.plot(x, y)

    # Salvar o gráfico em um buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    # Renderizar o gráfico em uma página HTML
    return render_template_string('<img src="data:image/png;base64,{{ plot_url }}"/>', plot_url=plot_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
