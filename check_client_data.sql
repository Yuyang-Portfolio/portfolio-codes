DECLARE @FiscalStart date = '2022-01-01'
DECLARE @FiscalEnd date = '2022-12-31'
 
-- Check client profile errors

SELECT DISTINCT SettlementPractitioner, ClientID, 'ERROR - date of birth OR immigration background' AS 'Message', max(date) AS 'Service Date'
      , DOB, ImmigrationCategoryName, ArrivalDateInCanada, CountryName, ArrivalDateInAlberta, LastProvinceCountryName
FROM ClientService.dbo.View_ClientServiceUnion GROUP BY ClientID, SettlementPractitioner, DOB, ImmigrationCategoryName, ArrivalDateInCanada
      , CountryName, ArrivalDateInAlberta, LastProvinceCountryName
HAVING (max(date) BETWEEN @FiscalStart AND @FiscalEnd) AND
      ((LastProvinceCountryName = 'Alberta'AND DOB <> ArrivalDateInAlberta) OR
      (LastProvinceCountryName <> 'Alberta' AND DOB = ArrivalDateInAlberta) OR
      (CountryName = 'Canada' AND DOB <> ArrivalDateInCanada) OR
      (CountryName <> 'Canada' AND DOB = ArrivalDateInCanada) OR
      (CountryName = 'Canada' AND ImmigrationCategoryName <> 'Citizen') OR
      (CountryName <> 'Canada' AND ImmigrationCategoryName = 'Citizen') OR
      (CountryName <> 'Canada' AND LastProvinceCountryName = 'Alberta') OR
      (ArrivalDateInCanada > ArrivalDateInAlberta) OR
      (DOB > ArrivalDateInCanada) OR  
      (DOB > ArrivalDateInAlberta))  
ORDER BY SettlementPractitioner, ClientID
