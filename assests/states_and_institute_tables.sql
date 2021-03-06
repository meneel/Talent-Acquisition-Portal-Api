USE [dummy]
GO
/****** Object:  Table [dbo].[InstituteMaster]    Script Date: 27-08-2021 23:29:43 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[InstituteMaster](
	[InstituteID] [nvarchar](50) NOT NULL,
	[InstituteName] [nvarchar](50) NOT NULL,
	[StateID] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_InstituteMaster] PRIMARY KEY CLUSTERED 
(
	[InstituteID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[StateMaster]    Script Date: 27-08-2021 23:29:43 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[StateMaster](
	[StateID] [nvarchar](50) NOT NULL,
	[StateName] [nvarchar](50) NOT NULL,
	[StateAbbreviation] [nvarchar](50) NOT NULL,
	[AltTag] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_StateMaster2] PRIMARY KEY CLUSTERED 
(
	[StateID] ASC,
	[StateAbbreviation] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[InstituteMaster] ([InstituteID], [InstituteName], [StateID]) VALUES (N'1', N'Indian Institute of Technology, Kharagpur', N'f619b152-918f-46fa-abca-da016905ec58')
INSERT [dbo].[InstituteMaster] ([InstituteID], [InstituteName], [StateID]) VALUES (N'2', N'Indian Institute of Management, Kolkata', N'f619b152-918f-46fa-abca-da016905ec58')
INSERT [dbo].[InstituteMaster] ([InstituteID], [InstituteName], [StateID]) VALUES (N'3', N'Indian Statistical Institute, Kolkata', N'f619b152-918f-46fa-abca-da016905ec59')
INSERT [dbo].[InstituteMaster] ([InstituteID], [InstituteName], [StateID]) VALUES (N'4', N'Indian Institute of Technology, Dhanbad', N'b2e3b4f1-1db8-4716-ab7f-70cb2f6ffd13')
GO
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'050ef318-5756-4eb7-98c5-f5e544cc869d', N'Lakshadweep', N'LD', N'IN-LD;LKP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'0b1e097d-0315-48c7-be0e-52bd802ea0e0', N'Haryana', N'HR', N'IN-HR')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'0bfc94ba-9b88-4729-831b-e59bb1f5b14e', N'Andaman and Nicobar Islands', N'AN', N'IN-AN')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'0fe91877-7b89-4869-8cf6-44fe970374ed', N'Uttar Pradesh', N'UP', N'IN-UP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'1c480d0d-a5af-4c0f-9227-ff6992dd6ca8', N'Bihar', N'BR', N'IN-BR')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'2f27848e-a198-418d-8f7d-da6f4b1433f9', N'Jammu and Kashmir', N'JK', N'IN-JK')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'3ef31277-ebb0-4d7b-bc71-2fdd02add97e', N'Chandigarh', N'CH', N'IN-CH;CHD')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'3f84f41c-886b-4cb6-8417-46e60a5871ca', N'Mizoram', N'MZ', N'IN-MZ;MIZ')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'4c84c733-848e-49c1-b6e0-328f4d4f612c', N'Kerala', N'KL', N'IN-KL;KER')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'55acee36-36c1-4a94-b276-1446f06f6aef', N'Meghalaya', N'ML', N'IN-ML;MEG')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'58236f79-afca-4c73-8301-1a3661236855', N'Karnataka', N'KA', N'IN-KA;KRN')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'5dc885f3-b7ed-4662-bdf4-6447c8239ec3', N'Delhi', N'DL', N'IN-DL;DEL')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'714c60d2-9496-4253-bf53-4e294e104e77', N'Rajasthan', N'RJ', N'IN-RJ;RAJ')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'71638e1a-cbb3-4cc1-a9f6-6f66b47518e5', N'Madhya Pradesh', N'MP', N'IN-MP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'83d66b14-c708-4acb-a9d7-f1fc29899064', N'Tamil Nadu', N'TN', N'IN-TN')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'9a596eb8-4b81-4e11-962c-3ba2273dd48e', N'Arunachal Pradesh', N'AR', N'IN-AR')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'9b8196c1-6413-4bf5-b771-67c89f027589', N'Maharashtra', N'MH', N'IN-MH;MAH')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'9cdb8020-23f3-4145-a6c6-50979f0611eb', N'Tripura', N'TR', N'IN-TR;TRP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'a801f728-184c-4abe-aa8f-cd560006523a', N'Daman and Diu', N'DD', N'IN-DD')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'ad30b097-3867-41bf-ae9a-bdd1d68d070e', N'Nagaland', N'NL', N'IN-NL;NLD')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'afdfad7a-7c73-4d51-bf06-b85e0f3c2fd5', N'Chhattisgarh', N'CT', N'IN-CT;CG')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'b2e3b4f1-1db8-4716-ab7f-70cb2f6ffd13', N'Jharkhand', N'JH', N'IN-JH')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'c1bbb235-9b0c-44a1-9c66-ed0317bd9785', N'Assam', N'AS', N'IN-AS')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'cff7b6cb-a9b4-4605-8909-f86511a05156', N'Sikkim', N'SK', N'IN-SK;SKM')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'd9f951c9-a00f-4eb3-ae53-e502bf3d7ba3', N'Andhra Pradesh', N'AP', N'IN-AP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'da501ae6-4f34-4924-abed-70c29cedc60f', N'Uttarakhand', N'UT', N'IN-UT;UK;UA;Uttaranchal')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'e29ed911-f265-4f06-a5e7-4333b000800d', N'Manipur', N'MN', N'IN-MN;MNP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'e443cf45-579d-40cf-9157-ea36a5698675', N'Odisha', N'OR', N'IN-OR;OD;Orissa')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'ebe88155-0b82-4167-8b07-fdb0f4a2ce0d', N'Dadra and Nagar Haveli', N'DN', N'IN-DN;DNH')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'ef592e91-aaad-477c-8471-a46a2b9d3644', N'Goa', N'GA', N'IN-GA')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'f1f224f8-9a1c-4317-9048-01ae1333ac5e', N'Gujarat', N'GJ', N'IN-GJ;GUJ')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'f619b152-918f-46fa-abca-da016905ec58', N'West Bengal', N'WB', N'IN-WB')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'fb019dac-d79b-4641-abe0-c7a8cbe7703b', N'Telangana', N'TG', N'IN-TG;TS')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'fc272f2a-d3cc-4431-8048-11a6a3dd961b', N'Himachal Pradesh', N'HP', N'IN-HP')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'fe41cfe0-aef9-4fa9-b730-94ed9336bff1', N'Puducherry', N'PY', N'IN-PY;PDY')
INSERT [dbo].[StateMaster] ([StateID], [StateName], [StateAbbreviation], [AltTag]) VALUES (N'fe667a10-07c5-4b55-b165-2ae8d28f87ea', N'Punjab', N'PB', N'IN-PB')
GO
