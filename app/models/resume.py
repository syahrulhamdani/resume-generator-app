"""Resume data models"""
from pydantic import BaseModel, Field


class JobExperience(BaseModel):
    """Job experience"""
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    date: str = Field(description="Date of employment")
    description: list[str] | str = Field(
        description="Description of job responsibilities"
    )


class Education(BaseModel):
    """Education"""
    degree: str = Field(description="Degree or qualification")
    institution: str = Field(description="Name of the institution")
    year: str = Field(description="Year of graduation")
    description: str | None = Field(
        default=None, description="Remarks on education"
    )


class ResumeData(BaseModel):
    """Resume data"""
    name: str = Field(description="Name of the resource")
    email: str | None = Field(default=None, description="Email address")
    phone: str | None = Field(default=None, description="Phone number")
    linkedin: str | None = Field(
        default=None, description="LinkedIn profile URL"
    )
    summary: str | None = Field(default=None, description="Executive summary")
    experience: list[JobExperience] = Field(description="Job experience")
    education: list[Education] | None = Field(
        default=None, description="Education"
    )
    skills: list[str] = Field(description="Skills")

