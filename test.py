import marimo

__generated_with = "0.17.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import sigdep.sigdep as sd
    sd.test()
    return


if __name__ == "__main__":
    app.run()
