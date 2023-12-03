// https://adventofcode.com/2023/day/2
use crate::common::SourceFile;
use regex::Regex;
use std::io;

struct Bag {
    red: u32,
    green: u32,
    blue: u32,
}

impl Bag {
    fn from_string(s: &str) -> Bag {
        let re = Regex::new(r"(\d+)\s(\w+)").unwrap();
        let captures = re.captures(s).unwrap();
        let mut bag = Bag {
            red: 0,
            green: 0,
            blue: 0,
        };

        for cap in re.captures_iter(s) {
            let colour = cap.get(2).unwrap().as_str();
            let value: u32 = cap.get(1).unwrap().as_str().parse::<u32>().unwrap();

            match colour {
                "red" => bag.red = value,
                "green" => bag.green = value,
                "blue" => bag.blue = value,
                _ => (),
            }
        }
        bag
    }
}

struct Game {
    id: u32,
    bags: Vec<Bag>,
}

fn parse_game(line: &str) -> Game {
    let re = Regex::new(r"^Game\s+(\d+)\D+(.+)$").unwrap();
    let captures = re.captures(line).unwrap();
    let id: u32 = captures.get(1).unwrap().as_str().parse::<u32>().unwrap();
    let bags_str: Vec<&str> = captures
        .get(2)
        .unwrap()
        .as_str()
        .split(r";")
        .collect::<Vec<&str>>();

    println!("id: {}", id);
    println!("bags_str: {:?}", bags_str);

    let mut game = Game {
        id: 0,
        bags: Vec::new(),
    };

    let mut bag = Bag {
        red: 0,
        green: 0,
        blue: 0,
    };

    let mut id = 0;
    let mut red = 0;
    let mut green = 0;
    let mut blue = 0;

    let mut i = 0;
    for c in line.chars() {
        match c {
            ' ' => (),
            ':' => (),
            ',' => (),
            _ => (),
        }
        i += 1;
    }

    game
}

fn either_part(file_path: &str) -> io::Result<i32> {
    let source = SourceFile::new(file_path).unwrap();
    parse_game(source.lines.first().unwrap());
    Ok(0)
}

fn part1(file_path: &str) -> io::Result<()> {
    let actual_bag = Bag {
        red: 12,
        green: 13,
        blue: 14,
    };
    either_part(file_path)?;
    println!("A message relating to Part 1");
    Ok(())
}

fn part2(file_path: &str) -> io::Result<()> {
    println!("A message relating to Part 2");
    Ok(())
}

pub fn run() -> io::Result<()> {
    println!("Day 02 of Advent of Code!");
    let file_path: &str = "src/day02/data/actual.txt";

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
    fn test_bag_from_string() {
        let bag = Bag::from_string(" 3 green, 15 blue, 14 red");
        assert_eq!(bag.red, 14);
        assert_eq!(bag.green, 3);
        assert_eq!(bag.blue, 15);
    }

    // #[test]
    // fn test_part1() {
    //     assert_eq!(part1("src/day02/data/test.txt").unwrap(), 8); // TODO: change this
    // }

    // #[test]
    // fn test_part2() {
    //     assert_eq!(part2("src/day02/data/test.txt").unwrap(), -9999); // TODO: change this
    // }
}
