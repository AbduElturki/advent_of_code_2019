proc readData {filename} {
    set f [open $filename r]
    set lines [lreplace [split [read $f] \n] end end]
    return $lines
}

proc getFuel {mass} {
    set total 0
    foreach i $mass {
        set total [expr max($i/3 - 2, 0) + $total ]
    }
    return $total
}

proc getFuelOfFuel {mass} {
    set total 0
    foreach i $mass {
        set j $i
        while {$j > 0} {
            set total [expr max($j/3 - 2, 0) + $total ]
            set j [expr max($j/3 - 2, 0)]
        }
    }
    return $total
}

proc main {} {
    set mass [readData input]
    set totalFuel [getFuel $mass]
    set totalFuelOfFuel [getFuelOfFuel $mass]
    puts "Total Fuel: $totalFuel"
    puts "Total Fuel of Fuel: $totalFuelOfFuel"
}

main
