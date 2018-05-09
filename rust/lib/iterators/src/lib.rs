pub struct Fibonacci {
    curr: u32,
    next: u32,
}

impl Fibonacci {
    pub fn new() -> Fibonacci {
        Fibonacci{curr: 1, next: 1}
    }
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
