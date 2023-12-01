use crate::common::SourceFile;
use regex::Regex;
use std::{io, num::ParseIntError};

enum DigitKind {
    Num,
    NumStr,
}

fn word_to_digit(word: &str) -> &str {
    match word {
        "one" => "1",
        "two" => "2",
        "three" => "3",
        "four" => "4",
        "five" => "5",
        "six" => "6",
        "seven" => "7",
        "eight" => "8",
        "nine" => "9",
        _ => word,
    }
}

fn process_line(line: &str, kind: &DigitKind) -> Result<i32, ParseIntError> {
    let regex_str = match kind {
        DigitKind::Num => r"\d",
        DigitKind::NumStr => r"\d|one|two|three|four|five|six|seven|eight|nine",
    };

    let re = Regex::new(regex_str).unwrap();

    // extract vector of matches
    let matches: Vec<&str> = re.find_iter(line).map(|mat| mat.as_str()).collect();

    // get first element
    let mut first = *matches.first().unwrap();
    first = word_to_digit(first);

    // get last element
    let mut last = *matches.last().unwrap();
    last = word_to_digit(last);

    // concatenate and parse
    let num_str = format!("{}{}", first, last);
    let num = num_str.parse::<i32>();
    num
}

fn process_lines(lines: Vec<String>, kind: &DigitKind) -> Result<Vec<i32>, ParseIntError> {
    let mut nums: Vec<i32> = Vec::new();

    for line in lines {
        let num = process_line(&line, &kind);
        match num {
            Ok(n) => nums.push(n),
            _ => (),
        }
    }

    Ok(nums)
}

fn either_part(file_path: &str, kind: DigitKind) -> Result<i32, ParseIntError> {
    let source = SourceFile::new(file_path).unwrap();
    let nums = process_lines(source.lines, &kind)?;

    let sum = nums.iter().sum::<i32>();
    Ok(sum)
}

fn part1(file_path: &str) -> io::Result<i32> {
    let sum: i32 = either_part(file_path, DigitKind::Num).unwrap();
    Ok(sum)
}

fn part2(file_path: &str) -> io::Result<i32> {
    let sum: i32 = either_part(file_path, DigitKind::NumStr).unwrap();
    Ok(sum)
}

pub fn run() -> io::Result<()> {
    println!("Day 01 of Advent of Code!");
    let file_path: &str = "src/day01/data/actual.txt";

    let part1 = part1(file_path)?;
    println!("Part 1: {:?}", part1);

    let part2 = part2(file_path)?;
    println!("Part 2: {:?}", part2);
    println!();

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("src/day01/data/test.txt").unwrap(), 142); // TODO: change this
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("src/day01/data/test_2.txt").unwrap(), 281); // TODO: change this
    }
}
