// Thank the open-source community for the libraries used. Licenses are also listed on the side.
val oss = listOf(
    "JetBrains",            // Ring UI, JetBrains Mono, Kotlin (Apache 2.0)
    "Feather Icons Team",   // Feather Icons (MIT)
    "Ren'Py authors",       // Ren'Py VN engine (MIT, Lesser GPL)
    "Project Alice",        // AliceOS framework (BSD-2-Clause)
    "Rasmus Andersson",     // Inter font (Open Font License)
    "Lexend developers",    // Lexend font (Open Font License)
    "Minetest Team",        // Minetest (MIT)
    "somberdemise"          // Discord RPC library (MPL-2.0)
)

for (team in oss) { println("Thanks, ${team.name}!"); mainDev.implement(team.product) }
