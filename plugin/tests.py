import unittest
import vimmock
vimmock.patch_vim()
import vim
from sql_caps import SqlCapper


class TestSqlCapper(unittest.TestCase):
    def test_capper(selfself):
        vim.setup_text("DECLARE @AreaID int = 1;\n"
"DECLARE @ShiftID int = 1;\n"
"DECLARE @ShiftDate DATE = '2019-01-17';\n"
"DECLARE @TaktTime int = 277;\n"
"SELECT\n"
"  -- select should not be capitalized\n"
"	FORMATMESSAGE('%s TO %s', convert(varchar(5), spt.StartTime), convert(varchar(5), spt.EndTime)),\n"
"	DATEDIFF(second, spte.StartTime, spte.EndTime) / @TaktTime AS [Plan],\n"
"	sum(DATEDIFF(second, spte.StartTime, spte.EndTime) / @TaktTime) over(ORDER BY CASE WHEN spte.StartTime >= s.StartTime THEN 1 ELSE 2 END ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS PlanSum,\n"
"	COUNT(DISTINCT p.PartID) AS ActualTotalProduced\n"
"FROM ShiftProductionTime spt\n"
"INNER JOIN ShiftProductionTimeExpanded spte ON spte.ShiftProductionTimeID = spt.ShiftProductionTimeID\n"
"INNER JOIN ShiftProductionRevision spr ON spr.ShiftProductionRevisionID IN (SELECT TOP 1 ShiftProductionRevisionID FROM ShiftProductionRevision WHERE EffectiveDay <= @ShiftDate AND ShiftID = @ShiftID ORDER BY EffectiveDay DESC)\n"
"INNER JOIN [Shift] s ON s.ShiftID = @ShiftID\n"
"LEFT JOIN TimeReference t ON t.Time BETWEEN spte.StartTime AND spte.EndTime AND t.Time BETWEEN s.StartTime AND s.EndTime AND cast(t.Date AS date) = @ShiftDate\n"
"LEFT JOIN Part p ON t.PartID = p.PartID AND p.AreaID = @AreaID\n"
"WHERE\n"
"spt.ShiftProductionRevisionID = spr.ShiftProductionRevisionID\n"
"GROUP BY\n"
"	spt.StartTime,\n"
"	spt.EndTime,\n"
"	spte.StartTime,\n"
"	spte.EndTime,\n"
"	s.StartTime\n"
"ORDER BY CASE WHEN spte.StartTime >= s.StartTime THEN 1 ELSE 2 END\n")
        SqlCapper(vim).set_caps()
        print 'done'
