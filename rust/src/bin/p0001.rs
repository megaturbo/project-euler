fn solve() -> u32{
    return (1..1000).filter(|&n| n % 3 == 0 || n % 5 == 0).sum::<u32>();
}

fn main() {
    println!("{}", solve());
}
