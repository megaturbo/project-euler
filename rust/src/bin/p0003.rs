// Prime iterator
impl Primes {
    pub fn new() -> Primes {
        Primes{val: 0}
    }
}

impl Iterator for Primes {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        self.val = self.val + 1;
        Some(self.val)
    }
}

fn solve() -> u64 {
    let n = 600851475143;
    let mut upper_limit = (n as f64).sqrt() as u64 + 1;
    let mut target = n;
    let mut factor = 2;
    while factor <= upper_limit {
        while target % factor == 0 {
            target = target / factor;
        }
        factor += 1;
        upper_limit = (target as f64).sqrt() as u64 + 1;
    }
    target
}

fn main() {
    println!("{:?}", solve());
}
