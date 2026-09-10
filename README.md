# UK Generations & Consumer Insight Quiz

## Introduction

The UK Generations & Consumer Insight Quiz is a Python application developed for use within my workplace. The application is designed to test and develop employees' knowledge of UK generational demographics and consumer characteristics through an interactive multiple-choice quiz.

The quiz uses demographic and population statistics from Statista reports, including data originally sourced from organisations such as the Office for National Statistics (ONS) and Ipsos.

<!-- Complete Introduction later: workplace context, business relevance, intended users and MVP purpose. Target: approximately 300 words. -->


## Design

### User Journey

```mermaid
flowchart TD
    A([Start]) --> B[Open UK Generations & Consumer Insight Quiz]
    B --> C[Enter participant name]
    C --> D{Name valid?}

    D -- No --> E[Display validation error]
    E --> C

    D -- Yes --> F[Complete 10-question quiz]
    F --> G{All questions answered?}

    G -- No --> H[Display incomplete quiz warning]
    H --> F

    G -- Yes --> I[Submit quiz]
    I --> J[Calculate score and percentage]
    J --> K{Score 70% or above?}

    K -- Yes --> L[Display Pass]
    K -- No --> M[Display Not yet passed]

    L --> N[Display category performance]
    M --> N

    N --> O[Display answer review]
    O --> P[Save result to CSV]
    P --> Q[Update results dashboard]
    Q --> R[View previous results and metrics]
    R --> S[Download results CSV]
    S --> T([End])
```

### Functional Requirements

| ID | Requirement |
|---|---|
| FR1 | The application shall allow a participant to enter their name. |
| FR2 | The application shall validate participant names before allowing the quiz to begin. |
| FR3 | The application shall load multiple-choice questions from persistent storage. |
| FR4 | The application shall allow the participant to answer quiz questions through a GUI. |
| FR5 | The application shall calculate and display the participant's score and percentage. |
| FR6 | The application shall save completed quiz results to persistent storage. |
| FR7 | The application shall allow stored results to be viewed. |
| FR8 | The application shall allow results to be exported. |

### Non-functional Requirements

| ID | Requirement |
|---|---|
| NFR1 | The application should provide a clear and easy-to-use interface. |
| NFR2 | Invalid user input should be handled without causing the application to crash. |
| NFR3 | Core application logic should be testable independently of the GUI. |
| NFR4 | The code should use meaningful names, type hints and descriptive docstrings. |
| NFR5 | Quiz results should persist between application sessions. |

### Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14.4 | Core programming language |
| Streamlit | Graphical user interface |
| pandas | CSV loading, manipulation and results analysis |
| pytest | Automated unit testing |
| Git/GitHub | Version control and remote repository |
| GitHub Actions | Continuous integration |
| CSV | Persistent question and result storage |

### Code Design

<!-- Add class diagram and explain Question, Quiz and data-management responsibilities. -->


## Development

### Object-Oriented Design

<!-- Explain Question and Quiz classes with selected code examples. -->

### Data Handling

<!-- Explain CSV question storage and pandas loading. -->

### Input Validation and Exception Handling

<!-- Explain pure validation functions, regex and exception handling. -->

### Graphical User Interface

<!-- Explain Streamlit implementation. -->


## Testing

### Testing Strategy

<!-- Explain TDD, unit testing, integration/manual testing and why each was selected. -->

### Test-Driven Development

<!-- Add RED/GREEN evidence captured during development. -->

### Automated Unit Testing

<!-- Add final pytest screenshot and explain important tests. -->

### Manual Testing

<!-- Add final manual testing table. -->

### Continuous Integration

<!-- Add GitHub Actions screenshot and explanation. -->


## Documentation

### User Documentation

<!-- Explain how an employee installs/opens and uses the application. -->

### Technical Documentation

<!-- Explain environment setup, dependencies, running the application and running tests. -->


## Evaluation

<!-- Reflect on successes, problems encountered, limitations and future improvements. -->