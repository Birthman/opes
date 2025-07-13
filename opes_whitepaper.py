from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Opes (XPS) Token White Paper", ln=True, align="C")
        self.ln(10)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

pdf = PDF()
pdf.add_page()

sections = [
    ("1. Introduction", 
     "Opes (XPS) is a utility token built on the Sui blockchain, designed to power an ecosystem where users are rewarded for participating in task-based activities and holding or staking tokens. With seamless integration into decentralized exchanges (DEXs) and a clear token utility path, Opes aims to build a sustainable, community-driven economy centered around active participation and long-term growth."),

    ("2. Project Overview",
     "The Opes token (XPS) will initially serve as a reward mechanism for users who complete tasks on the official Opes platform. This promotes real utility, user engagement, and community building from day one. As the project grows, XPS will support additional features such as staking, governance, and DeFi integration. Built on the fast and secure Sui blockchain, Opes is positioned for scalability and performance."),

    ("3. Tokenomics",
     "Total Supply: 1,000,000,000 XPS\n\n"
     "- Liquidity Pool - 300,000,000 XPS (30%)\n"
     "- Staking Rewards - 300,000,000 XPS (30%)\n"
     "- Marketing & Partnerships - 150,000,000 XPS (15%)\n"
     "- User Rewards & Airdrops - 100,000,000 XPS (10%)\n"
     "- Team & Development - 100,000,000 XPS (10%)\n"
     "- Treasury Reserve - 50,000,000 XPS (5%)\n\n"
     "This distribution ensures sufficient liquidity, generous incentives, and resources for growth and sustainability."),

    ("4. Use Cases",
     "- User Rewards: Earn XPS by completing verified tasks.\n"
     "- DEX and Exchange Trading: Tradeable on decentralized and centralized exchanges.\n"
     "- Staking: Earn passive income through staking.\n"
     "- Partnerships: Expand token utility via collaborations.\n"
     "- Future Governance: Participate in future proposals."),

    ("5. Roadmap",
     "- Q3 2025 - Token Creation & Initial DEX Listing\n"
     "- Q4 2025 - Launch of Task Reward System\n"
     "- Q1 2026 - Staking Platform Goes Live\n"
     "- Q2 2026 - Exchange Listings & Partner Integrations\n"
     "- Q3–Q4 2026 - Governance and DAO Framework"),  # <-- The '–' in Q3–Q4 is still en dash. Replace with hyphen:

    ("6. Team",
     "Founder & Developer: Victor Armstrong\n\n"
     "Victor Armstrong is the founder of the Opes (XPS) token project. With a background in mobile app development (6 completed apps) and a diploma in cybersecurity analysis, Victor brings technical experience in secure software development and blockchain implementation. He has also studied blockchain technology extensively, enabling him to build the XPS ecosystem on the Sui blockchain with a strong focus on user incentives, scalability, and long-term sustainability.\n\n"
     "The project is founded and led by Victor, with plans to expand the development team and advisory network as the ecosystem evolves."),

    ("7. Legal Disclaimer",
     "This document is for informational purposes only and does not constitute financial, legal, or investment advice. Cryptocurrencies are inherently volatile and involve risk. Potential participants should conduct their own research and consult with professionals before engaging in any token-related activities.\n\n"
     "The Opes (XPS) token is not intended to represent ownership, equity, or any claim to profits in any company or organization."),

    ("8. Contact",
     "- Website: [https://opesxps.org]\n"
     "- Email: [info@opesxps.org]\n"
     "- Twitter: [https://x.com/opes1182902?t]\n"
     "- Telegram: [https://t.me/opesxps]")
]

# Fix the Q3-Q4 en dash manually here:
sections[4] = (
    "5. Roadmap",
    sections[4][1].replace("–", "-")
)

for title, content in sections:
    pdf.chapter_title(title)
    pdf.chapter_body(content)

pdf.output("Opes_XPS_WhitePaper.pdf")
