// https://adventofcode.com/2022/day/1
use std::io;

use crate::common::SourceFile;

type Cals = Vec<i32>;

fn lines_to_cals(lines: Vec<String>) -> Cals {
    let mut cals: Cals = Vec::new();
    let mut current_cluster: i32 = 0;

    for line in lines {
        if line == "" {
            cals.push(current_cluster);
            current_cluster = 0;
        } else {
            let value: i32 = line.parse().unwrap();
            current_cluster += value;
        }
    }

    // Push the last cluster
    if current_cluster != 0 {
        cals.push(current_cluster);
    }

    cals
}

fn top_n_cals(mut cals: Cals, n: usize) -> Cals {
    cals.sort();
    cals.reverse();
    let top_n = cals[0..n].to_vec();
    top_n
}

fn either_part(file_path: &str, n: usize) -> io::Result<i32> {
    let source = SourceFile::new(file_path)?;
    let cals: Vec<i32> = lines_to_cals(source.lines);

    let binding = top_n_cals(cals, n);
    let max_cals = binding.iter().sum::<i32>();

    println!(
        "The {n} elf(s) with the highest calorie count is: {}",
        max_cals
    );
    Ok(max_cals)
}

fn part1(file_path: &str) -> io::Result<i32> {
    either_part(file_path, 1)
}

fn part2(file_path: &str) -> io::Result<i32> {
    either_part(file_path, 3)
}

pub fn run() -> io::Result<()> {
    println!("Day 00 of Advent of Code!");
    let file_path: &str = "src/day00/data/actual.txt";

    let part1 = part1(file_path)?;
    println!("Part 1: {}", part1);

    let part2 = part2(file_path)?;
    println!("Part 2: {}", part2);
    println!();

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("src/day00/data/test.txt").unwrap(), 24000);
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("src/day00/data/test.txt").unwrap(), 45000);
    }
}
