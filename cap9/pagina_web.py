filmes = {
    "Drama":["Cidadão Kane", "O Poderoso Chefão"],
    "Comédia": ["Tempos Modernos", "American Pie", "Dr Dolittle"],
    "Policial": ["Chuva Negra", "Desejo de Matar", "Dificil de Matar"],
    "Guerra": ["Rambo", "Platoon", "Tora!Tora!Tora!"]
}

with open("Filmes.html", "w", encoding = "UTF8") as pagina:
    pagina.write("""
<!DOCTYPE htmk>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
</head>
<body>
"""
    )
    for t, f in filmes.items():
        pagina.write(f"<h1>{t}</h1>\n")
        for e in f:
            pagina.write(f"<h2>{e}</h2>\n")
    pagina.write("</body></html>")
