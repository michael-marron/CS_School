from tutor_service import app

@app.route("/tutor-page", methods=["POST"])
def tutor_page():
    return render_template(
        "tutor-page.html",
    )

if __name__ == '__main__':
    app.run(debug=True)