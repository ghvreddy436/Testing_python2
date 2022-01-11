CREATE PROCEDURE my_sp
AS

begin

DECLARE @tableName varchar(50)
SET @tableName='Temp_Table'

DECLARE @SQL varchar(max)
SET @SQL = 'DROP TABLE ' + @tableName

EXEC('IF EXISTS(SELECT * FROM sys.tables WHERE type=''u'' and name = ''Temp_Table'') DROP TABLE Temp_Table')

SET @SQL= 'create table Temp_Table
(
latitude float,
longitude	float,
brightness	float,
scan	float,
track	float,
acq_date	date,
acq_time	int,
satellite	char(6),
confidence	float,
version	varchar(12),
bright_t31	float,
frp	float,
daynight char(8)
)
'
EXEC(@SQL)

end

go;