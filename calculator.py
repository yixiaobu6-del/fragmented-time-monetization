"""碎片时间变现计算器"""


class TimeValueCalculator:
    """碎片时间变现计算器，评估碎片时间的货币价值和可替代活动。"""

    def __init__(self, hourly_rate: float = 0, monthly_income: float = 0,
                 monthly_hours: float = 160):
        """初始化计算器。

        可通过直接传入时薪，或通过月收入/月工作时长推算时薪。

        Args:
            hourly_rate: 直接指定时薪（元/小时）
            monthly_income: 月收入（元），用于推算时薪
            monthly_hours: 月工作小时数，默认160小时
        """
        self.hourly_rate = hourly_rate or (monthly_income / monthly_hours if monthly_income > 0 else 0)

    def value_of(self, minutes: int, efficiency: float = 1.0) -> dict:
        """计算指定时长的价值及可完成的活动。

        Args:
            minutes: 时长（分钟）
            efficiency: 效率系数，1.0为100%

        Returns:
            包含时长、时薪、理论价值和可做事项的字典
        """
        hours = minutes / 60
        effective_hours = hours * efficiency
        monetary_value = effective_hours * self.hourly_rate

        opportunities = {
            "阅读": f"{int(minutes / 5)} 页书",
            "写作": f"{int(minutes * 20)} 字",
            "学习": f"{int(minutes / 25)} 个番茄钟",
            "沟通": f"{int(minutes / 15)} 次消息回复",
        }

        return {
            "时长": f"{minutes}分钟",
            "时薪": f"¥{self.hourly_rate:.0f}/h",
            "理论价值": f"¥{monetary_value:.1f}",
            "可以做的事": opportunities,
        }

    def annual_waste(self, daily_minutes: int) -> dict:
        """计算每日浪费时间的年度累积损失。

        Args:
            daily_minutes: 每日浪费时间（分钟）

        Returns:
            包含年度浪费小时数、工作日数和经济损失的字典
        """
        annual_minutes = daily_minutes * 365
        annual_hours = annual_minutes / 60
        annual_value = annual_hours * self.hourly_rate
        return {
            "每日浪费": f"{daily_minutes}分钟",
            "每年浪费": f"{annual_hours:.0f}小时",
            "相当于": f"{annual_hours / 8:.1f}个工作日",
            "经济损失": f"¥{annual_value:.0f}",
        }

    def compare_uses(self, minutes: int = 30) -> list:
        """对比不同用途的时间价值。

        Args:
            minutes: 时长（分钟），默认30分钟

        Returns:
            用途对比列表，每项包含用途名称、价值产出和长期收益评级
        """
        return [
            {"用途": "刷短视频", "价值产出": "¥0", "长期收益": "低"},
            {"用途": "学习新技能", "价值产出": f"¥{self.value_of(minutes)['理论价值']}", "长期收益": "高"},
            {"用途": "运动", "价值产出": "健康收益", "长期收益": "极高"},
            {"用途": "阅读", "价值产出": f"¥{minutes*20}字内容", "长期收益": "高"},
            {"用途": "社交", "价值产出": "人脉价值", "长期收益": "中"},
        ]


if __name__ == "__main__":
    calc = TimeValueCalculator(monthly_income=20000)
    print("=== 30分钟的价值 ===")
    for k, v in calc.value_of(30).items():
        print(f"  {k}: {v}")
    print("\n=== 每天浪费30分钟 ===")
    for k, v in calc.annual_waste(30).items():
        print(f"  {k}: {v}")
