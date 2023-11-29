# !/bin/bash

set -e

# get arg being the day to set up
DAY=$1

# print help if no args, or if first arg is -h or --help
if [ $# -eq 0 ] || [ $1 = "-h" ] || [ $1 = "--help" ]; then
    echo "Usage: setup_day.sh <day>"
    echo "day: the day to set up - must be greater than 0, and will be padded with 0 if less than 10"
    echo "e.g. setup_day.sh 1 -> sets up day01"
    exit 0
fi

# exit if day is not greater than 0
if [ $DAY -lt 1 ]; then
    echo "Day must be greater than 0"
    exit 1
fi

# pad with 0 if less than 10
printf -v DAY "%02d" $DAY
echo "Setting up Rust project for day $DAY"

# create dayDD folder within src, if it doesn't exist
DIR="src/day$DAY"
echo "Creating $DIR directory"
mkdir -p $DIR
mkdir -p $DIR/data

# Initialise module file
if [ ! -f "$DIR/mod.rs" ]; then
    echo "Creating $DIR/mod.rs"
    cat << EOF > $DIR/mod.rs
use std::io;
use crate::common::SourceFile;

pub fn part1() -> io::Result<_> {
    println!("Part 1");
    Ok(())
}

pub fn part2() -> io::Result<_> {
    println!("Part 2");
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        assert_eq!(part1("$DIR/data/test.txt").unwrap(), -9999); // TODO: change this
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2("$DIR/data/test.txt").unwrap(), -9999); // TODO: change this
    }
}
EOF
fi

if [ ! -f "$DIR/data/actual.txt" ]; then
    echo "Creating $DIR/data/actual.txt"
    echo "INPUT DATA GOES HERE" > $DIR/data/actual.txt
fi

if [ ! -f "$DIR/data/test.txt" ]; then
    echo "Creating $DIR/data/test.txt"
    echo "TEST DATA GOES HERE" > $DIR/data/test.txt
fi

echo "All necessary files created"

echo "Add the following to src/main.rs:\n"
echo "mod day$DAY;"
