"""
 Un hincha de fútbol desea conocer la cantidad de puntos que su equipo lleva acumulados en el campeonato, para ello recibe cada semana la
información de la cantidad total de partidos, desde el inicio del campeonato, que el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.
"""
partido_perdido = 0
partido_empatado = 1
partido_ganado = 3

suma_partido = partido_empatado + partido_ganado + partido_perdido

print(f"El equipo tiene {suma_partido} puntos acumulados")
