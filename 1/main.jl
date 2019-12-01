function getFuel(mass)
    total = 0
    for i in mass
       total = max(floor(parse(Int, i)/3) - 2, 0) + total
    end
    return Int(total)
end

function getFuelOfFuel(mass)
    total = 0
    for i in mass
       j = parse(Int, i)
       while j > 0
           total = max(floor(j/3) - 2, 0) + total
           j = max(floor(j/3) - 2, 0)
        end
    end
    return Int(total)
end

function main()
    f = open("input")
    mass = readlines(f)
    totalFuel = getFuel(mass)
    totalFuelOfFuel = getFuelOfFuel(mass)
    println("total fuel: ", totalFuel)
    println("total fuel of fuel: ", totalFuelOfFuel)
end

main()
