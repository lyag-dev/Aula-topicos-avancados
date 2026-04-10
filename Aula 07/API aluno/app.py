from flask import Flask, jsonify, request, render_template, redirect
from veiculo import Veiculo

app = Flask(__name__)

veiculos = []

veiculo_1 = Veiculo("Fiat", "uno", "123abc", 2003, 19000)
veiculos.append(veiculo_1)

@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", veiculos=veiculos)

@app.route("/veiculo", methods=["GET"])
def listar_veiculos():
    return jsonify([veiculo.to_dict() for veiculo in veiculos])

@app.route("/veiculo", methods=["POST"])
def adicionar_veiculo():
    marca = request.form["Marca"]
    modelo = (request.form["Modelo"])
    placa = (request.form["Placa"])
    ano = int((request.form["Ano"]))
    preco = int((request.form["Preço"]))

    novo_veiculo = Veiculo(marca, modelo, placa, ano, preco)
    veiculos.append(novo_veiculo)

    return redirect("/")

@app.route("/remover/<int:id>")
def remover_aluno(id):
    global veiculos
    veiculo = [veiculo for veiculo in veiculos if veiculo.id != id]
    return redirect("/")

# Rota para carregar os dados de um veiculo
@app.route("/editar/<int:id>")
def editar_veiculo(id):
    veiculo = next((veiculo for veiculo in veiculos if veiculo.id == id), None)
    if veiculo:
        return render_template("editar.html", veiculo=veiculo)
    return redirect("/")

# Rota para atualizar um veiculo
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_veiculo(id):
    veiculo = next((veiculo for veiculo in veiculos if veiculo.id == id), None)
    if veiculo:
        marca = request.form["Marca"]
        modelo = (request.form["Modelo"])
        placa = (request.form["Placa"])
        ano = int((request.form["Ano"]))
        preco = int((request.form["Preço"]))
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)