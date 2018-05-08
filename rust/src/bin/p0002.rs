extern crate num_traits;

struct Fibonacci {
    curr: u32,
    next: u32,
}

impl Iterator for Fibonacci {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        let next = self.curr + self.next;
        self.curr = self.next;
        self.next = next;
        Some(self.curr)
    }
}

fn solve(bound: u32) -> u32 {
    Fibonacci{curr: 1, next: 1}
        .take_while(|&n| n < bound)
        .filter(|&n| n % 2 == 0)
        .sum()
}

fn main() {
    println!("{:?}", solve(4000000));
}
