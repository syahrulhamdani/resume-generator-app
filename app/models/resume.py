"""Resume data models"""
from pydantic import BaseModel, Field


class JobExperience(BaseModel):
    """Job experience"""
    title: str = Field(description="Job title")
    company: str = Field(description="Company name")
    date: str = Field(description="Date of employment")
    description: list[str] | str = Field(
        description="List of projects done / responsibilities during the job"
    )


class Certification(BaseModel):
    """Certification"""
    name: str = Field(description="Name of the certification")
    organization: str = Field(description="Certificate provider")
    date: str = Field(description="Date of certification")


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
    title: str = Field(description="Title of the resource")
    email: str | None = Field(default=None, description="Email address")
    phone: str | None = Field(default=None, description="Phone number")
    linkedin: str | None = Field(
        default=None, description="LinkedIn profile URL"
    )
    github: str | None = Field(default=None, description="GitHub profile URL")
    website: str | None = Field(default=None, description="Website URL")
    summary: str | None = Field(default=None, description="Executive summary")
    experience: list[JobExperience] = Field(description="Job experience")
    education: list[Education] | None = Field(
        default=None, description="Education"
    )
    skills: dict[str, list[str]] = Field(description="Skills")
    certifications: list[Certification] | None = Field(
        default=None, description="Certifications"
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "John Doe, Ph.D.",
                    "title": "Senior AI & Machine Learning Consultant",
                    "email": "john.doe@example.com",
                    "phone": "(123) 456-7890",
                    "linkedin": "linkedin.com/in/johndoe",
                    "github": "github.com/johndoe",
                    "website": "johndoe.ai",
                    "summary": "Innovative AI strategist with 8+ years of experience delivering business-critical machine learning solutions across financial services, healthcare, and tech sectors. Specialized in NLP, computer vision, and generative AI applications that drive measurable business outcomes.",
                    "experience": [
                        {
                            "title": "Lead AI Consultant",
                            "company": "Global AI Solutions",
                            "date": "Jan 2021 - Present",
                            "description": [
                                "Lead a team of 12 data scientists implementing enterprise-scale AI solutions for Fortune 500 clients",
                                "Architected and deployed a GPT-based customer service solution reducing response time by 75% and saving $2.5M annually",
                                "Designed computer vision systems for quality control, improving defect detection accuracy by 32%",
                                "Advised C-suite executives on AI strategy and roadmap development across 6 major organizations"
                            ]
                        },
                        {
                            "title": "Senior AI Engineer",
                            "company": "Tech Innovations Inc.",
                            "date": "Mar 2018 - Dec 2020",
                            "description": [
                                "Developed NLP algorithms for sentiment analysis improving market prediction accuracy by 28%",
                                "Built and optimized ML pipelines processing 50TB of daily data using Spark and TensorFlow",
                                "Created reinforcement learning models for algorithmic trading with 18% improved returns",
                                "Mentored junior team members and led bi-weekly knowledge sharing sessions"
                            ]
                        },
                        {
                            "title": "Machine Learning Researcher",
                            "company": "AI Research Lab",
                            "date": "Jun 2016 - Feb 2018",
                            "description": [
                                "Conducted research on deep learning approaches for medical image analysis",
                                "Published 4 peer-reviewed papers in top-tier ML conferences (NeurIPS, ICML)",
                                "Developed a novel CNN architecture reducing training time by 40% while maintaining accuracy",
                                "Collaborated with interdisciplinary teams of physicians and engineers on healthcare AI applications"
                            ]
                        }
                    ],
                    "education": [
                        {
                            "degree": "Ph.D. in Artificial Intelligence",
                            "institution": "Stanford University",
                            "year": "2016",
                            "description": "Thesis: 'Novel Deep Learning Architectures for Natural Language Understanding'. GPA: 3.95/4.0"
                        },
                        {
                            "degree": "M.S. in Computer Science",
                            "institution": "Massachusetts Institute of Technology",
                            "year": "2012",
                            "description": "Specialization in Machine Learning and Data Science. GPA: 4.0/4.0"
                        },
                        {
                            "degree": "B.S. in Computer Engineering",
                            "institution": "University of California, Berkeley",
                            "year": "2010",
                            "description": "Minor in Mathematics. Graduated with High Honors. GPA: 3.92/4.0"
                        }
                    ],
                    "skills": {
                        "AI/ML": ["Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Reinforcement Learning", "Generative AI", "LLMs"],
                        "Programming": ["Python", "TensorFlow", "PyTorch", "JAX", "Keras", "SQL", "R", "Java", "C++"],
                        "Cloud & Big Data": ["AWS", "GCP", "Azure ML", "Kubernetes", "Docker", "Spark", "Hadoop", "Airflow"],
                        "Tools & Platforms": ["MLflow", "Weights & Biases", "DVC", "Kubeflow", "Ray", "Hugging Face", "OpenAI API"]
                    },
                    "certifications": [
                        {
                            "name": "AWS Certified Machine Learning – Specialty",
                            "organization": "Amazon Web Services",
                            "date": "May 2022"
                        },
                        {
                            "name": "Professional Machine Learning Engineer",
                            "organization": "Google Cloud",
                            "date": "October 2021"
                        },
                        {
                            "name": "Azure AI Engineer Associate",
                            "organization": "Microsoft",
                            "date": "March 2021"
                        },
                        {
                            "name": "Deep Learning for Computer Vision",
                            "organization": "NVIDIA Deep Learning Institute",
                            "date": "July 2020"
                        }
                    ],
                    "publications": [
                        "Doe, J. et al. (2022). 'Transformer Architectures for Large-Scale Medical Image Analysis.' NeurIPS 2022.",
                        "Doe, J. and Smith, A. (2020). 'Self-Supervised Learning for Time Series Forecasting.' ICML 2020.",
                        "Doe, J. et al. (2018). 'Attention Mechanisms in Medical Diagnosis Systems.' IEEE Trans. Medical Imaging."
                    ],
                    "languages": [
                        {"language": "English", "proficiency": "Native"},
                        {"language": "Mandarin Chinese", "proficiency": "Professional working proficiency"},
                        {"language": "Spanish", "proficiency": "Conversational"}
                    ]
                } 
            ]
        }
    }
