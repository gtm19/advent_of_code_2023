use std::fs::File;
use std::io::{self, BufRead};

pub struct SourceFile {
    pub lines: Vec<String>,
}

impl SourceFile {
    pub fn new(file_path: &str) -> io::Result<Self> {
        let lines = read_lines(file_path)?;
        Ok(Self { lines })
    }
}

fn read_lines(file_path: &str) -> io::Result<Vec<String>> {
    let file = File::open(file_path)?;
    let lines = io::BufReader::new(file).lines().collect::<Result<_, _>>()?;
    Ok(lines)
}
