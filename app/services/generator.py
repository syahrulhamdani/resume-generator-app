"""Resume generator service."""
import logging
from time import time
from typing import List, Dict, Union

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table

from app.services.style import Style

_LOGGER = logging.getLogger(__name__)


class ResumeGenerator:
    """Resume generator service."""
    def __init__(self, style: Style):
        """Initialize the resume generator with styles

        Args:
            style: Style configuration for the resume
        """
        self.style = style

    def generate_pdf(self, resume_data: Dict, output_path: str) -> None:
        """
        Generate a PDF resume from the provided data

        Args:
            resume_data: Dictionary containing resume information
            output_path: Path where the PDF should be saved
        """
        t0 = time()
        _LOGGER.info("Start building resume")
        try:
            doc = SimpleDocTemplate(output_path, pagesize=letter)
            content = self._build_content(resume_data)
            doc.build(content)
        except Exception as exc:
            _LOGGER.error("Error generating PDF: %s", exc)
            raise
        _LOGGER.info("Done building resume in %.2fs", time() - t0)

    def _build_content(self, resume_data: Dict) -> List:
        """Build the PDF content from resume data"""
        content = []

        # Add header with name and contact info
        self._add_header(content, resume_data)

        # Add summary if available
        if resume_data.get('summary'):
            self._add_section(
                content, 'Professional Summary', resume_data['summary']
            )

        # Add skills if available
        if resume_data.get('skills'):
            self._add_skills(content, resume_data['skills'])

        # Add experience if available
        if resume_data.get('experience'):
            self._add_experience(content, resume_data['experience'])

        # Add education if available
        if resume_data.get('education'):
            self._add_education(content, resume_data['education'])

        return content

    def _add_header(self, content: List, resume_data: Dict) -> None:
        """Add header with name and contact information"""
        name = resume_data.get('name', '')
        content.append(Paragraph(name, self.style.name))
        title = resume_data.get('title', '')
        content.append(Paragraph(title, self.style.title))

        # Contact information
        contact_info = []
        if resume_data.get('email'):
            contact_info.append(resume_data['email'])
        if resume_data.get('phone'):
            contact_info.append(resume_data['phone'])
        if resume_data.get('linkedin'):
            contact_info.append(resume_data['linkedin'])

        if contact_info:
            content.append(
                Paragraph(' | '.join(contact_info), self.style.contact_info)
            )

    def _add_section_title(self, content: List, title: str) -> None:
        """Add a section title with an underline."""
        # Add the section title
        content.append(Paragraph(title, self.style.section_header))

        # Add horizontal line under the section title
        separator = Table([[""]],
                          colWidths=[6.5*inch],  # Adjust width as needed
                          rowHeights=[0])
        separator.setStyle(self.style.section_title_line)
        content.append(separator)

    def _add_section(self, content: List, title: str, text: str) -> None:
        """Add a simple section with title and content"""
        self._add_section_title(content, title)
        content.append(Paragraph(text, self.style.normal))

    def _add_experience(
        self, content: List, experience_list: List[Dict]
    ) -> None:
        """Add experience section"""
        self._add_section_title(content, 'Professional Experience')

        for job in experience_list:
            job_title = job.get('title', '')
            company = job.get('company', '')
            date_range = job.get('date', '')

            # Create a table with job title on left, date on right
            title_paragraph = Paragraph(f"{job_title} - {company}",
                                        self.style.item_title)
            date_paragraph = Paragraph(date_range, self.style.item_subtitle)

            # Create a table with one row and two columns
            job_table = Table([[title_paragraph, date_paragraph]], 
                              colWidths=[4*inch, 2.5*inch])
            job_table.setStyle(self.style.job_table)

            content.append(job_table)

            # Add responsibilities/achievements
            if job.get('description'):
                if isinstance(job['description'], list):
                    for item in job['description']:
                        bullet = self.style.get_bullet_point()
                        content.append(Paragraph(f"{bullet} {item}",
                                                 self.style.bullet_point))
                else:
                    content.append(Paragraph(job['description'],
                                             self.style.normal))

    def _add_education(
        self, content: List, education_list: List[Dict]
    ) -> None:
        """Add education section"""
        self._add_section_title(content, 'Education')

        for edu in education_list:
            degree = edu.get('degree', '')
            institution = edu.get('institution', '')
            year = edu.get('year', '')

            # Create a table with degree on left, year on right
            degree_paragraph = Paragraph(degree, self.style.item_title)
            year_paragraph = Paragraph(year, self.style.item_subtitle)

            # Create a table with one row and two columns
            edu_table = Table(
                [[degree_paragraph, year_paragraph]],
                              colWidths=[4*inch, 2.5*inch])
            edu_table.setStyle(self.style.job_table)
            
            content.append(edu_table)
            content.append(Paragraph(institution, self.style.normal))

            if edu.get('description'):
                content.append(Paragraph(edu['description'], self.style.normal))

    def _add_skills(
        self, content: List, skills: Union[List[str], Dict[str, List[str]]]
    ) -> None:
        """Add skills section"""
        self._add_section_title(content, 'Skills')

        if isinstance(skills, list):
            # Format skills as a paragraph with commas
            skills_text = ", ".join(skills)
            content.append(Paragraph(skills_text, self.style.normal))
        elif isinstance(skills, dict):
            # Handle categorized skills
            for category, skills_list in skills.items():
                content.append(
                    Paragraph(
                        f"<b>{category}:</b> {', '.join(skills_list)}",
                        self.style.normal
                    )
                )
