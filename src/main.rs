use std::collections::HashMap;
use std::fs::{File, OpenOptions};
use std::io::{self, BufRead, Read, Write};
use regex::Regex;

fn main() -> io::Result<()> {
    
    // 打开 seg.so 文件
    let mut file = File::open("seg.so")?;
    
    // 创建一个缓冲区以存储文件内容
    let mut buffer = Vec::new();
    
    // 读取文件内容到缓冲区
    file.read_to_end(&mut buffer)?;

    // 尝试将字节数据转换为字符串
    let content = String::from_utf8_lossy(&buffer);
    
    // 正则表达式匹配中文字符、大小写英文字符和 emoji
    let re = Regex::new(r"[\u4e00-\u9fa5\p{So}]+").unwrap();

    // 创建一个列表以存储匹配的字符串
    let mut matched_strings = Vec::new();

    // 输出所有匹配的字符串并存储到列表
    for cap in re.captures_iter(&content) {
        let matched = &cap[0];
        // 排除不可见字符
        if !matched.contains('\u{FFFD}') {
            matched_strings.push(matched.to_string());
        }
    }
 
    // 创建一个 HashMap 来存储词频
    let mut word_count = HashMap::new();

    // 处理每个字符串
    for string in matched_strings {
        // 将字符串分割成词
        for word in string.split_whitespace() {
            // 将词转换为字符串并更新词频
            let count = word_count.entry(word.to_string()).or_insert(0);
            *count += 1;
        }
    }

    // 打开或创建一个 txt 文件用于写入输出
    let mut output_file = OpenOptions::new()
        .write(true)
        .create(true)
        .truncate(true)
        .open("output1.txt")?;

    // 输出词频到文件
    for (word, count) in &word_count {
        writeln!(output_file, "{}: {},", word, count)?;
    }

    // 打开 py.txt 文件
    let path = "py.txt";
    let file2 = File::open(path)?;
    let reader = io::BufReader::new(file2);

    // 创建一个 HashMap 来存储词频
    let mut word_count = HashMap::new();

    // 逐行读取文件内容
    for line in reader.lines() {
        let line = line?;
        // 将行分割成词
        for word in line.split_whitespace() {
            // 将词转换为字符串并更新词频
            let count = word_count.entry(word.to_string()).or_insert(0);
            *count += 1;
        }
    }

    // 打开或创建一个 txt 文件用于写入输出
    let mut output_file = OpenOptions::new()
        .write(true)
        .create(true)
        .truncate(true)
        .open("output2.txt")?;

    // 输出词频到文件
    for (word, count) in &word_count {
        writeln!(output_file, "{}: {}", word, count)?;
    }
    Ok(())
}
