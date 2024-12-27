# HR Analytics: Employee Attrition & Performance

## 📝 Introduction 
In the business world, keeping talented employees is a big challenge. One major issue is the growing problem of employee turnover, often called HR attrition. High turnover can seriously affect a company's productivity and stability. It can lead to higher hiring and training costs, disrupt teamwork, and cause the loss of valuable knowledge within the company. That's why it's so important to understand what drives attrition and to put effective retention strategies in place to stay competitive and ensure long-term success.

## 💡 Objective
- Check the Current Turnover Rates: Start by getting a clear picture of the current employee turnover rate. Break it down by factors like age, gender, education level, department, and job role to spot any patterns.

- Find the Main Reasons for Turnover: Look into the key reasons employees leave. This includes job satisfaction aspects like involvement and work-life balance, salary-related factors such as monthly pay and raises, and benefits like stock options. Analyzing these factors can help uncover trends that lead to higher turnover.

## ⚙ Approach/Steps
### 1. Ask
**Business Task -** to uncover patterns and correlations that drive higher attrition rates.

**Tools:** <br>
- Data Wrangling - Excel & Python.
- Exploratory Data analysis - Python.
- Data visualization - Python.

### 3. Process
The original dataset has 1470 rows and 35 columns.<br>
![Screenshot 2024-12-12 145904](https://github.com/user-attachments/assets/b750501f-3e19-45a4-8e3f-a89b35b6ea8d)

### 4. Analyze
> 1. What is the total Attrition Rate in the company?
#### Attrition Rate in the company
![Attrition rate](https://github.com/user-attachments/assets/9b057f62-10cc-456b-832c-b1fec9600506)

- Attrition rate of the company is 16.12%

> 2. What is the attrition rate as per Age and Gender?
#### Attrition Rate by Age & Gender
![Attrition by age and gender](https://github.com/user-attachments/assets/d383ecef-c8e6-4a18-bf1d-6207de02319f)

- Younger employees, especially those in the 30-35 age group, appear to be more likely than other age groups to leave a company.
- Male employees tend to leave more often than female employees.

> 3.  What is the attrition rate as per Education?
#### Attrition Rate by Education
![education](https://github.com/user-attachments/assets/06d457b1-d89c-4a2b-bdce-d0053f30fa08)

- Lower turnover rate of employees with master's and doctoral degrees.

> 3.  What is the attrition rate as per Department and Job role?
#### Attrition Rate by Department and Job role
![Department](https://github.com/user-attachments/assets/523ec7f3-5fa2-4fef-8e92-265d56b360ec)
![job role](https://github.com/user-attachments/assets/22d18327-a651-42b9-b7b2-bb998d750787)

- The sales department, along with roles like sales representatives and lab technicians, experiences high turnover rates.
- The research and development department and the positions of research scientist and research director have low turnover rates.

> 4. What is the attrition rate based on Satisaction Factor?
#### Attrition Rate based on Satisfaction factor
![satisfaction](https://github.com/user-attachments/assets/ed77651b-cb05-40d9-8dde-1e72496022ee)

- **Job Satisfaction:** Employees with low job satisfaction are more likely to leave, indicating that factors like tasks, responsibilities, and challenges play a key role in retention.  
- **Environmental Satisfaction:** An unsupportive or uncomfortable work environment, or one that conflicts with an employee's values, can drive them to seek other opportunities.  
- **Relationship Satisfaction:** Positive relationships with colleagues and supervisors foster a sense of belonging and loyalty, helping reduce turnover.  
- **Job Involvement:** Employees who are engaged and invested in their work tend to remain loyal and committed to the organization.  
- **Work-Life Balance:** Maintaining a healthy work-life balance is crucial. Employees who feel that work negatively impacts their personal lives are more likely to leave.  

> 4. What is the attrition rate based on Salary Factor?
#### Attrition Rate based on Salary factor
![salary](https://github.com/user-attachments/assets/4f44800e-1798-4884-94b0-a3027415ff39)
 
- This chart reveals that the majority of employees who left earned a monthly income between 5,000 and 7,500. Turnover rates significantly decline for employees earning above 7,500, suggesting that higher salaries are linked to greater employee retention.
- The chart indicates that employees with salary increases below 16% are more likely to leave the company.

> 5. What is the attrition rate based on Beneit factor?
#### Attrition Rate based on Benefit factor
![beneit](https://github.com/user-attachments/assets/7a06b964-27d1-4fd9-b186-43bcbb1ab152)

- **Stock options:** contribute positively to employee retention, as those with more shares are generally more loyal and remain with the company longer. 
- **Training opportunities:** ample training opportunities enhance employee satisfaction and motivation, encouraging them to stay with the organization.

> 6. What is the attrition rate between new hires and long-time employees?
#### Attrition rate between new nies and long-time employees
![yearAt company](https://github.com/user-attachments/assets/00245b02-42a9-4cd8-9dcd-3537a36e8aea)

The data reveals that new employees face a significantly higher risk of leaving the company compared to those with longer tenure. The high attrition rate within the first year underscores the importance of focused retention strategies for new hires. Furthermore, employees with approximately 20 and 35 years of service also exhibit noticeable spikes in attrition, warranting targeted attention during these periods.

> 7. How other factors like Distance from home and Marital status affects attrition?
#### Attrition based on Distance From Home and Marital Status
![distanve and marital status](https://github.com/user-attachments/assets/775114ad-cb17-4f2c-a638-95b4a5cd2eb7)

- **Distance from home:** The turnover rate varies significantly across different distances. While no clear linear pattern emerges, the graph reveals sharp increases in turnover rates at specific distances. This indicates that the distance to work could be a contributing factor in an employee's decision to leave the company.
- **Marital Status:** Single employees exhibit the highest turnover rate, followed by married employees, while divorced employees have the lowest turnover rate. This suggests that marital status could be a factor influencing an employee's decision to remain with or leave the company.

> 8. How attrition rate is affected by Travel frequency of the employee?
#### Attrition rate based on Business travel
![travel frequency](https://github.com/user-attachments/assets/e666077a-a7b2-40d9-9356-a2ffb6b7c9c4)

> 9. How attrition rate is related to number of years an employee worked under the current manager?
#### Attrition rate based on Years under current manager
![years with CM](https://github.com/user-attachments/assets/63b6a1e8-7abb-4e25-9216-8df1abc38006)

> 10. How attrition rate is related to promotion?
#### Attrition rate based on Years since last promotion
![since lat promo](https://github.com/user-attachments/assets/601bc0b3-c242-42dc-bea6-447c6cc46884)

> 11. How educational field affects attrition rate?
#### Attrition rate based on Educational field
![Education field](https://github.com/user-attachments/assets/d00dc1c2-19e8-4047-809d-4cc9be287227)

> 12. How Over time affects the  attrition?
#### Attrition rate based on Over Time
![overtime](https://github.com/user-attachments/assets/0cf6fdbb-bcf7-4f4f-8940-8cbc0c580593)

> 13. How does the number of companies an employee has previously worked for impact attrition?
#### Attrition Rate based No.of companies an employee worked
![no of compaines worked](https://github.com/user-attachments/assets/be1bd756-f923-47db-a891-a33446447cdd)




