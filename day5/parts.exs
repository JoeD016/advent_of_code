defmodule AdventOfCode.Solution.Year2022.Day05 do
    def part1() do
        solve("input1.txt", &Enum.reverse/1)
        |> IO.puts()
    end

    def part2() do
        solve("input2.txt", &Function.identity/1)
        |> IO.puts()
    end


    def solve(input, crane_fn) do 
        [board, moves] = 
        File.read!(input)
        |> String.split("\n\n")
        stacks = parse_board(board)
        moves = parse_instrs(moves)
        moves
        |> Enum.reduce(stacks, &move(&1, &2, crane_fn))
        |> Enum.sort_by(fn {stack_label, _stack} -> stack_label end)
        |> Enum.map(fn {_stack_label, [crate | _]} -> crate end)
        |> to_string()
        |> IO.puts()
    end

    defp move({source, dest, count}, stacks, crane_fn) do
        {to_move, to_remain} = Enum.split(stacks[source], count)

        stacks
        |> Map.put(source, to_remain)
        |> Map.update!(dest, &Enum.concat(crane_fn.(to_move), &1))
    end

    defp parse_board(board) do
        board
        |> String.split("\n", trim: true)
        |> Enum.reverse()
        |> Enum.drop(1)
        |> Enum.map(&parse_row/1)
        |> Enum.reduce(fn stacks_row, stacks ->
            Map.merge(stacks, stacks_row, fn _stack_label, stack, [crate] -> [crate | stack] end)
        end)
    end

    defp parse_row(row) do
        row
        |> String.to_charlist()
        |> Enum.drop(1)
        |> Enum.take_every(4)
        |> Enum.with_index(fn (crate, i) -> {i + 1, [crate]} end)
        |> Enum.reject(&match?({_stack_label, ' '}, &1))
        |> Map.new()
    end

    defp parse_instrs(instr_lines) do
        instr_lines
        |> String.split("\n", trim: true)
        |> Enum.map(fn line ->
            ~r/^move (\d+) from (\d) to (\d)$/
            |> Regex.run(line, capture: :all_but_first)
            |> Enum.map(&String.to_integer/1)
            |> then(fn [count, from_label, to_label] -> {from_label, to_label, count} 
        end)
    end)
  end

end

AdventOfCode.Solution.Year2022.Day05.part2