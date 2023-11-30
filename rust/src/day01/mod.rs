use std::io;
use crate::common::SourceFile;

fn part1() -> io::Result<_> {
    println!("Part 1");
    Ok(())
}

fn part2() -> io::Result<_> {
    println!("Part 2");
    Ok(())
}

pub fn run() -> io::Result<()> {
    println!("Day 01 of Advent of Code!");
    let file_path: &str = "src/day01/data/actual.txt";

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
        assert_eq!(part1("src/day01/data/test.txt").unwrap(), -9999); // TODO: change this
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("src/day01/data/test.txt").unwrap(), -9999); // TODO: change this
    }
}
