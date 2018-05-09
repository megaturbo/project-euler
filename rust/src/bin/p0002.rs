extern crate iterators;

use iterators::Fibonacci;

fn solve(bound: u32) -> u32 {
    Fibonacci::new()
        .take_while(|&n| n < bound)
        .filter(|&n| n % 2 == 0)
        .sum()
}

fn main() {
    println!("{:?}", solve(4000000));
}
