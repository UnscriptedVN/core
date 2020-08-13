/*
    Unscripted Credits
    (C) 2020 Katorin Trenda.
 */
import dev.unscriptedvn.contributors.*
println("Unscripted VN")
println("A VN about software development")

val mainDev = Developer("Marquis Kurt")
mainDev.develop(withLove=true)

val artists = listOf(Artist("Minikle", "background"), Artist("Raseruuu", "sprites"))
for (artist in artists) { artist.draw() }

val musicians = listOf(Musician("Stray Objects"), Musician("Marek Domagala"))
for (musician in musicians) { musicians.compose() }
