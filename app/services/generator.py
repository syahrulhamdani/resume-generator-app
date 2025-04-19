"""Resume generator service."""
import logging
from typing import List, Dict, Union, Optional

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle


class ResumeGenerator:
    """Resume generator service."""
    def __init__(self):
        """Initialize the resume generator with styles"""
        self.styles = getSampleStyleSheet()
        self.title_style = self.styles['Heading1']
        self.heading_style = self.styles['Heading2']
        self.subheading_style = self.styles['Heading3']
        self.normal_style = self.styles['Normal']

        # Custom styles
        self.section_title_style = ParagraphStyle(
            'SectionTitle',
            parent=self.styles['Heading2'],
            spaceAfter=10,
            textColor=colors.darkblue
        )

    def generate_pdf(self, resume_data: Dict, output_path: str) -> None:
        """
        Generate a PDF resume from the provided data

        Args:
            resume_data: Dictionary containing resume information
            output_path: Path where the PDF should be saved
        """
        try:
            doc = SimpleDocTemplate(output_path, pagesize=letter)
            content = self._build_content(resume_data)
            doc.build(content)
        except Exception as exc:
            logging.error("Error generating PDF: %s", exc)
            raise

    def _build_content(self, resume_data: Dict) -> List:
        """Build the PDF content from resume data"""
        content = []
        
        # Add header with name and contact info
        self._add_header(content, resume_data)
        
        # Add summary if available
        if resume_data.get('summary'):
            self._add_section(content, 'Professional Summary', resume_data['summary'])
        
        # Add experience if available
        if resume_data.get('experience'):
            self._add_experience(content, resume_data['experience'])
        
        # Add education if available
        if resume_data.get('education'):
            self._add_education(content, resume_data['education'])
        
        # Add skills if available
        if resume_data.get('skills'):
            self._add_skills(content, resume_data['skills'])
        
        return content

    def _add_header(self, content: List, resume_data: Dict) -> None:
        """Add header with name and contact information"""
        name = resume_data.get('name', '')
        content.append(Paragraph(name, self.title_style))
        title = resume_data.get('title', '')
        content.append(Paragraph(title, self.subheading_style))

        # Contact information
        contact_info = []
        if resume_data.get('email'):
            contact_info.append(resume_data['email'])
        if resume_data.get('phone'):
            contact_info.append(resume_data['phone'])
        if resume_data.get('linkedin'):
            contact_info.append(resume_data['linkedin'])

        if contact_info:
            content.append(Paragraph(' | '.join(contact_info), self.normal_style))
        content.append(Spacer(1, 0.2 * inch))

    def _add_section(self, content: List, title: str, text: str) -> None:
        """Add a simple section with title and content"""
        content.append(Paragraph(title, self.section_title_style))
        content.append(Paragraph(text, self.normal_style))
        content.append(Spacer(1, 0.2 * inch))

    def _add_experience(self, content: List, experience_list: List[Dict]) -> None:
        """Add experience section"""
        content.append(Paragraph('Professional Experience', self.section_title_style))

        for job in experience_list:
            job_title = job.get('title', '')
            company = job.get('company', '')
            date_range = job.get('date', '')

            content.append(Paragraph(f"<b>{job_title} - {company}</b>", self.normal_style))
            content.append(Paragraph(f"<i>{date_range}</i>", self.normal_style))

            # Add responsibilities/achievements
            if job.get('description'):
                if isinstance(job['description'], list):
                    for item in job['description']:
                        content.append(Paragraph(f"• {item}", self.normal_style))
                else:
                    content.append(Paragraph(job['description'], self.normal_style))

            content.append(Spacer(1, 0.1 * inch))

        content.append(Spacer(1, 0.1 * inch))

    def _add_education(self, content: List, education_list: List[Dict]) -> None:
        """Add education section"""
        content.append(Paragraph('Education', self.section_title_style))

        for edu in education_list:
            degree = edu.get('degree', '')
            institution = edu.get('institution', '')
            year = edu.get('year', '')

            content.append(Paragraph(f"<b>{degree}</b>", self.normal_style))
            content.append(Paragraph(f"{institution}, {year}", self.normal_style))

            if edu.get('description'):
                content.append(Paragraph(edu['description'], self.normal_style))

            content.append(Spacer(1, 0.1 * inch))

    def _add_skills(self, content: List, skills: Union[List[str], Dict[str, List[str]]]) -> None:
        """Add skills section"""
        content.append(Paragraph('Skills', self.section_title_style))

        if isinstance(skills, list):
            # Format skills as a paragraph with commas
            skills_text = ", ".join(skills)
            content.append(Paragraph(skills_text, self.normal_style))
        elif isinstance(skills, dict):
            # Handle categorized skills
            for category, skills_list in skills.items():
                content.append(Paragraph(f"<b>{category}:</b> {', '.join(skills_list)}", self.normal_style))
                content.append(Spacer(1, 0.05 * inch))
