from flask import Flask, jsonify, request, render_template, redirect
from veiculo import Veiculo

app = Flask(__name__)

veiculos = []

veiculo_1 = Veiculo("Fiat", "uno", "123abc", 2003, 19000)
veiculos.append(veiculo_1)

@app.route("/", methods=["GET"])
def pagina_inicial():
    return render_template("index.html", veiculo=veiculos)

@app.route("/veiculo", methods=["GET"])
def listar_alunos():
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
    global alunos
    alunos = [aluno for aluno in alunos if aluno.id != id]
    return redirect("/")

# Rota para carregar os dados de um aluno
@app.route("/editar/<int:id>")
def editar_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno.id == id), None)
    if aluno:
        return render_template("editar.html", aluno=aluno)
    return redirect("/")

# Rota para atualizar um aluno
@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar_aluno(id):
    aluno = next((aluno for aluno in alunos if aluno.id == id), None)
    if aluno:
        aluno.nome = request.form["nome"]
        aluno.idade = int(request.form["idade"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)