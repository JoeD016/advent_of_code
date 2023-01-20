defmodule AdventOfCode.Solution.Year2022.Day04 do
    def part1() do 
        File.read!("input1.txt")
        |> String.split("\n", trim: true)
        |> Enum.map(&parse_line/1)
        |> Enum.count(&qualify?/1)
        |> IO.puts()
    end

    def part2() do 
        File.read!("input2.txt")
        |> String.split("\n", trim: true)
        |> Enum.map(&parse_line/1)
        |> Enum.count(&overlap?/1)
        |> IO.puts()
    end
    defp parse_line(line) do
        line
        |> String.split(",")
        |> Enum.map(&parse_int/1)
    end

    defp parse_int(input) do
        input
        |> String.split("-")
        |> Enum.map(&String.to_integer/1)
    end

    defp qualify?([[a,b],[x,y]]) do
        (a <= x and b >= y) or (x <= a and y >= b)
    end

    defp overlap?([[a,b],[x,y]]) do
        not Range.disjoint?(a..b, x..y)
        # (a <= x and x <= b) or (x <= a and a <= y)
    end
end

AdventOfCode.Solution.Year2022.Day04.part2