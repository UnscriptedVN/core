/*
    Unscripted Credits
    (C) 2020 Katorin Trenda.
 */
import net.marquiskurt.unscripted.contributors.*
println("Unscripted VN")
println("A VN about software development")

val mainDev = Developer("Marquis Kurt")
mainDev.develop(withLove=true)

val artists = listOf(Artist("Minikle", "background"), Artist("Raseruuu", "sprites"))
for (artist in artists) { artist.draw() }

val musician = Musician("Stray Objects")
musician.compose()
