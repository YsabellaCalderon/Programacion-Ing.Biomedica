import funciones_tarea_noticia as support
lineas = support.read_news ("noticia.txt")
support.mostrar_lineas(lineas)

Text = ["Desde el punto de vista profesional, considero que el potencial de almeida\n"
"a pesar de no tener principalmente una carrera profesinal, es impresionante\n"
"el hecho de crear una nueva tecnica con el microscopio en su epoca, que le permitiera\n"
"observar e investigar distintas celulas como lo fue el coronavirus\n"
"le brindan grandes aportes a la ciencia, ademas del empoderamiento femenino\n"
"que funciona como ejemplo para muchas mujeres con los mismos objetivos\n"]

support.escribir_noticia ("opinion.txt",Text)
