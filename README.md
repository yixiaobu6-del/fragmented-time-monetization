# 碎片时间变现计算器

> 利用碎片时间创造价值的收益计算与可视化分析工具

---

## Features / 功能特点

| 功能 | 说明 |
|------|------|
| 时间设置 | 自定义每天碎片时间（10-240分钟）和每月工作天数 |
| 变现方式 | 支持写短文/录短视频/回答咨询/写代码/翻译/设计/配音/在线辅导 |
| 实时计算 | 自动计算日收益/月收益/年收益预估 |
| 收益对比 | 各变现方式收益柱状图可视化对比 |
| 详细分析 | 每种方式的时薪、效率、月收益、年收益排行 |
| 数据持久化 | localStorage 记录偏好的变现方式设定 |

## Installation / 安装

无需安装，直接在浏览器中打开 `index.html` 即可使用。

```bash
# 克隆仓库
git clone https://github.com/yourusername/fragmented-time-monetization.git

cd fragmented-time-monetization
open index.html
```

## Usage / 使用方法

### 基础用法

1. 打开 `index.html`
2. 设置每天可用的碎片时间和工作天数
3. 选择感兴趣的变现方式（可多选）
4. 查看自动计算的收益预估和对比图表

### 收益计算示例

```javascript
// 收益计算逻辑
function calculateIncome(source, dailyMinutes, workDaysPerMonth) {
  const rates = {
    "写短文": 50,        // 时薪（元/小时）
    "录短视频": 80,
    "回答咨询": 100,
    "写代码": 150,
    "翻译": 70,
    "设计": 90,
    "配音": 60,
    "在线辅导": 120
  };
  const hourlyRate = rates[source];
  const dailyHours = dailyMinutes / 60;
  const monthlyHours = dailyHours * workDaysPerMonth;
  
  return {
    daily: dailyHours * hourlyRate,
    monthly: monthlyHours * hourlyRate,
    yearly: monthlyHours * hourlyRate * 12
  };
}
```

### 各变现方式收益对比

| 变现方式 | 时薪估算 | 碎片时间效率 | 适合人群 |
|----------|:--------:|:------------:|----------|
| 写短文 | 50 元/h | 高 | 写作者 |
| 录短视频 | 80 元/h | 中 | 创作者 |
| 回答咨询 | 100 元/h | 高 | 专业人士 |
| 写代码 | 150 元/h | 低 | 程序员 |
| 翻译 | 70 元/h | 中 | 语言人才 |
| 设计 | 90 元/h | 中 | 设计师 |
| 配音 | 60 元/h | 中 | 声音条件好 |
| 在线辅导 | 120 元/h | 高 | 教育背景 |

## Contributing / 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)

## License / 许可证

MIT License - 参见 [LICENSE](LICENSE)

---

> 版本：1.0.0 | 更新日期：2026-05-30