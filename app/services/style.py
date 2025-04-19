"""Resume style service."""
from dataclasses import dataclass

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import TableStyle


@dataclass
class Style:
    """Resume style configuration."""
    # Document colors
    primary_color: str = colors.black
    secondary_color: str = colors.gray

    # Font configurations
    default_font: str = "Helvetica"
    bold_font: str = "Helvetica-Bold"
    italic_font: str = "Helvetica-Oblique"
    default_font_size: int = 10

    # Additional style options
    bold_section_titles: bool = True
    use_bullet_points: bool = True
    bullet_character: str = "•"

    # Updated separator line configurations with darker color
    separator_color: str = colors.black
    separator_thickness: float = 0.75
    separator_space_before: int = 8
    separator_space_after: int = 12

    def __post_init__(self):
        """Initialize the actual styles based on configuration."""
        self.styles = getSampleStyleSheet()

        # large and centered
        self.name = ParagraphStyle(
            "Name",
            fontName=self.bold_font,
            fontSize=22,
            alignment=1,  # center alignment
            spaceAfter=14,
        )
        # below name - smaller and centered
        self.title = ParagraphStyle(
            "Title",
            fontName=self.default_font,
            fontSize=11,
            alignment=1,  # center alignment
            spaceAfter=6,
        )
        self.contact_info = ParagraphStyle(
            "ContactInfo",
            fontName=self.default_font,
            fontSize=9,
            alignment=1,  # center alignment
            spaceAfter=20,
        )
        self.normal = ParagraphStyle(
            "Normal",
            fontName=self.default_font,
            fontSize=self.default_font_size,
        )
        self.section_header = ParagraphStyle(
            'SectionHeader',
            fontSize=12,
            spaceBefore=20,
            spaceAfter=6,
            textColor=self.primary_color,
            fontName=self.bold_font,
            textTransform="uppercase",
            alignment=0,
        )
        # Experience/Education title style (bold)
        self.item_title = ParagraphStyle(
            'ItemTitle',
            fontName=self.bold_font,
            fontSize=10,
            alignment=0,
            spaceBefore=8,
        )
        # Experience/Education subtitle style (italic)
        self.item_subtitle = ParagraphStyle(
            'ItemSubtitle',
            fontName=self.italic_font,
            fontSize=10,
            alignment=2,
        )
        # Date style (right-aligned)
        self.date = ParagraphStyle(
            'Date',
            fontName=self.italic_font,
            fontSize=10,
            alignment=2,
            spaceBefore=10,
            spaceAfter=8,
        )
        # Bullet points style
        self.bullet_point = ParagraphStyle(
            'BulletPoint',
            fontName=self.default_font,
            fontSize=10,
            leftIndent=20,
            firstLineIndent=-10,
            spaceBefore=2,
            spaceAfter=2,
        )

        # Add a table style for job entries
        self.job_table = TableStyle([
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 0),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ])

        # Update horizontal line style for section titles
        self.section_title_line = TableStyle([
            ('LINEABOVE', (0, 0), (-1, 0),
             self.separator_thickness, self.separator_color),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('TOPPADDING', (0, 0), (-1, -1), self.separator_space_before),
            ('BOTTOMPADDING', (0, 0), (-1, -1), self.separator_space_after),
        ])

    def get_bullet_point(self) -> str:
        """Returns the bullet character if bullet points are enabled."""
        return self.bullet_character if self.use_bullet_points else ""
