from pathlib import Path
import json,re,hashlib
R=Path.cwd();run=R/'graphify-out/runs/2026-10-15-typography-consumers-final';files=json.loads((run/'chunk-00.files.json').read_text());old=json.loads((run/'before/graph.json').read_text());plan=json.loads((run/'semantic-plan.json').read_text())
def norm(s):return re.sub('[^a-z0-9]','_',s.lower())
def stem(p):return norm(str(Path(p).relative_to(R).with_suffix('')))
def fresh():return dict(nodes=[],edges=[],hyperedges=[],input_tokens=0,output_tokens=0,usage_status='UNAVAILABLE')
g=fresh();roots={};keys={};edgekeys=set()
def node(i,k,label,kind='concept',**a):
 p=files[i];ident=stem(p)+'_'+norm(k);n=dict(id=ident,label=label,file_type=kind,source_file=p,source_location=None,source_url=None,captured_at=None,author=None,contributor=None);n.update(a);g['nodes'].append(n);keys[(i,k)]=ident;return ident
def edge(a,b,i,rel='references',confidence='EXTRACTED',score=1.0,**a2):
 k=(a,b,rel,files[i])
 if k in edgekeys:return
 edgekeys.add(k);d=dict(source=a,target=b,relation=rel,confidence=confidence,confidence_score=score,source_file=files[i],source_location=None,weight=1.0);d.update(a2);g['edges'].append(d)
def fact(i,k,label,kind='concept',**a):
 n=node(i,k,label,kind,**a);edge(roots[i],n,i);return n
meta=[
('Repository SDD authority and closure rules',{'protocol_version':'0.4.0'}),
('Contextual Button recovery preparer',{'status':'PREPARADOR_LOCAL','execution_claim':'No Figma execution or validation credited by this preparer'}),
('CONTPAQi reusable web library',{'families':43,'scope':'Local UI and sample data, no product backend'}),
('Generated typography reference0.1.2',{'status':'DERIVED_NOT_AUTHORITY','styles':79,'catalog_version':'0.1.2','catalog_sha256':'074a31a83f09b30a02fa8b8f0a7730bdb33fc0a8a9c59e3c8d2469b5799e934c'}),
('Web component CSS role and state composition',{'scope':'Semantic role/recipe/state/geometry coupling; not imports'}),
('P07 reusable web component delivery',{'protocol_version':'0.3.2'}),
('Documentary native inheritance QA0.1.2',{'result':'PASS','scope':'Documentary only','contract_status':'DELEGATED_FOR_BUILD','human_audit':'PENDING'}),
('Historical typography consumers0.1.1',{'status':'PARTIAL / BLOCKED_BY_USAGE_LIMIT','historical':True,'current_pointer':'qa/implementations/typography.v0.1.2.review.md'}),
('Current typography consumers0.1.2',{'result':'PASS','scope':'Verified typography and captured preservation controls','human_audit':'PENDING','remote_library_published':False}),
('Contextual recovery QA',{'scope':'66 contextual labels, separate canonical/box/ink criteria','historical':True}),
('Checkbox five-sixths causal pilot',{'result':'CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT','scope':'One consumer; no implicit103 acceptance'}),
('Checkbox two-thirds causal pilot',{'result':'CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT','scope':'One consumer; no implicit103 acceptance'}),
('Count four-thirds causal pilot',{'result':'CAUSAL_INHERITANCE_SUPPORTED_FOR_THIS_PILOT','checks':12,'scope':'One consumer; no normative approval implicit'}),
('Native inheritance103 evidence QA',{'result':'PASS','scope':'Evidence only; does not itself modify contracts'}),
('Native-description cards visual review',{'result':'PASS_SCOPED','scope':'Three cards and final two prefix clarifications'}),
('Four underline cards visual review',{'result':'PASS_SCOPED','scope':'Four new cards, not consumer census'}),
('Historical Graphify closure preparation',{'status':'READ_ONLY_PLAN','historical':True,'prepare_executed':False,'close_executed':False}),
('Historical native inheritance amendment proposal',{'status':'LOCAL_PROPOSAL_NOT_ACTIVE_NORM','historical':True,'human_audit':'PENDING'}),
('Historical provisional skills0.2.1 candidate',{'result':'PASS_FOR_THIS_CUT','historical':True,'published':False,'current_at_cut':'0.2.0'}),
('Historical release0.2.1 preparation',{'status':'PREPARED_NOT_PUBLISHED_OR_INSTALLED','historical':True,'scaled_at_cut':'103 BLOCKED'}),
('Web typography revision79 QA',{'result':'PASS','catalog_version':'0.1.1','scope':'Web measured scope, not Figma consumption'}),
('Final skills release0.2.1 QA',{'package_status':'CURRENT','installed_status':'CURRENT','offline_result':'PASS','new_figma_screen':'NOT_RUN','human_audit':'PENDING'})]
for i,(title,a) in enumerate(meta):roots[i]=node(i,'artifact_'+Path(files[i]).suffix[1:],title,'code' if i==4 else 'document',**a)
# Named concepts and mechanisms from the fully read documents. Historical state remains local to its source.
D={
0:[
('authority','SDD single-source authority','Markdown governs rules; referenced canonical JSON governs delegated data. Inventories, observed Figma, code and Graphify are evidence, not authority. Conflicting approved sources produce CONFLICT and stop affected operation.'),
('delegation','Bounded migration delegation','Legacy9zs5RMR8LB5wHjW9Bd59BA to destinationtj3WIBEZDGLVs7MJWKCwgf; DELEGATED_FOR_BUILD is not human APPROVED. Source contracts, token mapping and QA required; human audit PENDING.'),
('slots_gate','Slots applicability gate','REQUIRED, justified NOT_APPLICABLE or UNRESOLVED per family. Variable quantity/composition matters; named frames or exposed instances alone do not prove native Slots.'),
('typography','Active shared typography0.1.2','Catalog0.1.2 is the one editable owner of recipe and description. New local text selects among18base by function; existing component complementaries remain restricted.'),
('native','Bounded native style consumption','Direct style ID or scoped native evidence: actual principal, chain, scale, metrics and no incompatible overrides. Empty local ID alone is insufficient; never assign materialized recipe again to native scaled instance.'),
('skills','Paired versioned skills','contpaqi-figma-screens and contpaqi-po-prototypes share DS cut; sync/check/export and authorized managed installation are required closure deliverables. Historical skills and edited user copies are preserved.'),
('graph','Complete graph closure','Graphify is derived. Full structural+semantic coverage, hashes, integrity, report/HTML/manifest and queries are required before CURRENT; AST-only is insufficient for documents. Failures retain backup and STALE/BLOCKED.'),
('tokens','Semantic token identity','Preserve aliases/bindings and original IDs. BENI/NAVI only use fixed character-identity exceptions. Nearest primitive requires semantic role, not direct fill; historical inventory is immutable.')],
1:[
('allowlist','66-identity contextual recovery allowlist','Input Fields6, Modal36, Empty States16, Conversation8. Only unscaled UI single ranges joined to canonical mapping and complete SHA page guard.'),
('transforms','Three exact contextual tracking restorations','14 ui-action-label-small→ui-label-compact-bold;44 ui-action-label-medium→ui-action-label-normal;8 ui-action-label-medium-underline→ui-action-label-normal-underline. Tracking0.1%→0px; family, weight,size,line-height,decoration unchanged.'),
('geometry','One measured FileUpload geometry ledger','I420:299;26:104 restores x8→9 and width122→121 with exact matrix/bounding-box tuples. Button154×32, Dropzone and Success unchanged. No general1px tolerance.'),
('readback','Fresh complete readback after sequential range setters','Rematerialize nodes to avoid invalidated proxies; read all nodes even after setter failure; retain mutation report. No metric/geometry/decoration/property setters. PASS_PAGE_GUARD_GLOBAL_READBACK_REQUIRED is not global validation.'),
('tests','Preparer software validation','25 recovery scenarios and33 guard scenarios plus parse/hash checks are mock/software evidence, not execution in Figma.')],
2:[
('runtime','Pinned local web runtime','Next16.4.0, React19.3.0, Tailwind4.3.3, TypeScript7.0.2; verified Node24.19.0/pnpm11.25.0/Chrome. No global Node install or remote package publication.'),
('client','Controlled presentation and Client Component boundary','Serializable server data may be passed; events/local state belong to Client Components. Reload resets sample data; no fiscal rules, permissions, remote uploads or AI responses simulated.'),
('assets','Reusable sources themes and assets','Copy components/lib/generated/index/styles plus public/assets, preserve relationships and runtime/PostCSS dependencies. data-ds-theme supports contable/administrativo/servicios/personas; logo/character identity colors unaffected.72/72 logos local.'),
('portable','Catalog HTTP versus portable HTML','Ordinary Next out/index.html requires HTTP for routes. PO skill is separate standalone file:// compiler; README does not claim raw Next catalog is portable.'),
('typography','Typed shared typography consumer','79styles=18base+61complementary fromcatalog0.1.2. typographyClass(id) includes decoration; --ds-type-style-id supports inspection. Three materialized recipes apply once; Figma needs independent native-link proof.'),
('gate','Per-family coverage and maintenance gate','43families require export, types, documentation and compiled example; ds:generate compares current sources/hashes/coverage. Build/interactions do not prove every variant, pixel identity or complete WCAG.')],
3:[
('authority','Generated typography single source','DERIVED_NOT_AUTHORITY; canonical JSON0.1.2 owns metrics/names/description. Regenerate with ds:generate; do not edit this Markdown.'),
('api','Typed typography and CSS inspection API','typographyClass, typography and TypographyId expose recipe identity. --ds-type-ID-font combines family/weight/size/line-height; tracking/decoration remain explicit; --ds-type-style-id is inspectable.'),
('units','Unit-preserving web conversion','Line-height PERCENT/100→unitless; tracking PERCENT/100→em; PIXELS→px; AUTO→normal. AUTO requires actual font/consumer verification; tokenRefs alone do not prove Figma binding.'),
('base','18 general hierarchy styles','Choose by function, not equal size: headings1–5, subheadings1–2, Body and Caption. All base tracking−2%.'),
('complementary','61 restricted compatibility styles','Preserve documented roles/instances and contractual geometry. Matching size does not justify arbitrary use as a general scale.'),
('format','Four underline style derivations','derivedFormattingFrom changes textDecoration only; family/weight/size/lineHeight/tracking/tokenRefs remain same. Consume -underline identity, not later format override.'),
('scale','Three materialized Float32 recipes','2/3,5/6,4/3 already included in recipe; recipeScale1. Do not transform:scale or multiply again. Native Figma consumes principal style through proven chain/scale rather than assigning materialized recipe.')],
5:[
('deliverable','Per-family web delivery requirements','Reusable typed export, canonical tokens/typography, technical docs, executable sample without backend, applicable QA. Required on additions/modifications; no implicit design or publishing permission.'),
('assignment','Role and range typography assignment','Consume base+family amendments, logical identity, resolved metrics/decoration and units. No isolated editable CSS catalog. New local text uses18base; existing complementary usage stays restricted.'),
('slots','React composition is distinct from native Slots','children/ReactNode/stable typed collections support insert/remove/reorder where appropriate. This mechanism does not prove a Figma native Slot.'),
('validation','Destination-specific validation','Typecheck/build prove compilation only. Test affected interactions, variants, layouts and typography. Web PASS does not validate Figma linkage, all geometry or universal visual fidelity.'),
('closure','Web skill and graph closure chain','Regenerate→typecheck/build→affected browser QA→document scope→P08pairedsync/check/export/installauthorized→P05fullgraph. Do not close with outdated skills.')],
6:[
('integrity','Documentary native amendment integrity','PASS:19changedsourcehashes,43familyspecs preserved,six evidence reports. Contract DELEGATED_FOR_BUILD/human auditPENDING; no Figma calls in this review.'),
('catalog_diff','Restricted catalog0.1.2 difference','79recipes/IDs/names/metrics/bindings/units/decoration/factors preserved. Only3description,3derivedFrom.reason,encoding explanation and version/provenance changed; finalSHA074a31a8….'),
('scope','Explicit native replacement scope','REQ-TYP-004/AC-TYP-004 and TYC-01/06 with13assignmentgroups across Select,Dropdown Item,Header,App Shell.43familyamendments andmapping0.1.1 bytes preserved.'),
('handoff','Nine native handoff regressions','9PASS: sources/hash tampering,missingnativeevidence,unknownstyle,nocapture. Carries actual reportstatus andresult, keeps new destinationNOT_RUN. Synthetic tests do not prove browser/Figma/install.'),
('docs','Documentary check at review cut','PASS1073JSON/272frontmatter,21historicalfindings+4preexistingwarnings. Distribution and graph currentness have separate evidence.')],
7:[
('historical_scope','Historical direct and scaled QA split','0.1.1 cut:3250directranges in3248nodesPASS;150editorialpreserved;103scaledBLOCKED under direct-ID rule althoughmetricsmatch.43families39consuming4excluded;3351UInodes/3353UIranges.'),
('usage_limit','Historical Count usage-limit interruption','ReadA was not executed due to tool usage limit, not safety rejection. NoBwrite; Countroots1063:1392/1414 remained at this cut. Later0.1.2 review resolves state; historical body remains intact.'),
('chat','Chat72 link correction','72oldlinks corrected under complete1119-node pageguardPASS; finalselection retains33censuspages and replaces only Chat.'),
('table','Lost historical Table nontext guard','1446UIranges read back with IDs and35externalpages preserved. Timeout prevented retrieval of complete inside-Table nontext guard; cannot retroactively reconstruct missing property comparison.')],
8:[
('coverage','Current3353-range typography closure','PASS34pages/3351UInodes/3353ranges:3250direct+103provennative,0unresolved;150editorialpreserved.79styles18base61complementary;43families39consuming4excluded.'),
('native','Current103 native style consumption','LocalIDsremainempty truthfully. Require actualprincipalstyle,APIchain,nativescale,effectiverecipe,noincompatibleoverrides andcausalproof. No fabricatedID or secondderivedstyleassignment.'),
('limits','Current preservation limits','Tablelostnontextguard remains unverified; historicalliteralinkFAILs retained. ThisPASS does not certify alldesign, universalclippingabsence, humanaudit orremotepublication.'),
('cleanup','Three causal pilots restored and cleaned','Checkbox2/3,Checkbox5/6,Count4/3 complete36controls,originalguardsequal,exactrestoration,alltemporaryrootsremoved including1063:1392/1414.'),
('catalog','Current79 shared styles and documentation','ThreeTextStyledescriptions,threecards,eightstatusreferences synchronized;80localrecipes preserved includinghistoricalstyleoutside79catalog. Webappliesmaterializedrecipeonce;Figma provesnativebinding independently.')],
9:[
('criteria','Independent canonical box and ink criteria','CanonicalID/recipe/bindings; originaldimensions/preservationhash; literalabsoluteRenderBounds are different results. A canonicalPASS and historicalinkFAIL may coexist without general geometry tolerance.'),
('counts','66 recovered contextual labels','FileUpload6(6direct0inherited),Modal36(4direct32inherited),Empty16(8direct8inherited),Conversation8(4direct4inherited):22direct44inherited.'),
('guards','Historical contextual page guard results','FileUploadPASSwithboundedledger. ModalFAIL36nodedifferenceswithoutpersistedfielddetail. EmptyFAIL14with10completeinkdiagnosticsand4truncated. ConversationFAIL2completeink-onlydiagnostics.66canonicalpostchecksPASS separately.'),
('geometry','Observed FileUpload exact restoration','I420:299;26:104 width122→121/x8→9 with5exacttuples; Button154×32 unchanged;clonecleaned andoriginalschecked. No general1pxtolerance.'),
('ink','Rendered ink interpretation','Tracking0.1%→0 reducesglyphspacing: at16px interval0.016px; at14px0.014px. Empty/Conversation derived explanation backedbyactualinkdiagnostics; Modal remainsINFERRED becausefieldsnotpersisted.'),
('limit','Contextual result does not replace global census','66postchecks and33guard/25recoverysoftwaretests do not validateallconsumers or103scaled. Source ends with finalindependentcensus pending; do not rewrite as currentglobalPASS.')],
10:[
('route','Actual Checkbox5/6 main route','Original446:167→API main149:179; actor149:180/control149:183. Ownercomponentset andinstance cloned; actualchildrenroute verified.'),
('causal','Checkbox5/6 causal A→B→A','Onlycopiedmainactor receivesui-body-compact→subheading-1-semibold→A. IndependentreadskeepinstanceIDempty;Bpropagates16.66666603088379/SemiBold600/LH150%/tracking−2%;A restores11.666666030883789/LH16.66666603088379px/0px.'),
('restoration','Checkbox5/6 exact restoration and cleanup','Control,properties,overrides,scale unchanged;fullArestoredfields/hashes andoriginalguardsequal;bothrootsdeleted. Onlyobservedrootemptyrefs andexactlocalnameoverride normalized; noconsumerwrite.')],
11:[
('route','Actual Checkbox2/3 main route','Original446:207→API main149:179; actor149:180/control149:183. Ownercomponentset andinstance cloned; actualchildrenroute verified.'),
('causal','Checkbox2/3 causal A→B→A','Onlycopiedmainactor receivesui-body-compact→subheading-1-semibold→A. IndependentreadskeepinstanceIDempty;Bpropagates13.333333969116211/SemiBold600/LH150%/tracking−2%;A restores9.333333969116211/LH13.333333969116211px/0px.'),
('restoration','Checkbox2/3 exact restoration and cleanup','Control,properties,overrides,scale unchanged;fullArestoredfields/hashes andoriginalguardsequal;bothrootsdeleted. Onlyobservedrootemptyrefs andexactlocalnameoverride normalized; noconsumerwrite.')],
12:[
('route','Actual Count4/3 main route','SourceDotmain155:136/text155:137,control155:135;copiedDotowner+IconButtoninstance. Actualmain/childrenverified. Twoexactobserved redundantlayoutPositioning/nameoverrideentriesnormalized onlywithunchangedvalues;initialfailurepreserved.'),
('causal','Count4/3 causal A→B→A','Onlycopiedmainactor receivesmicro-count-small→ui-metric-value-small→A. Bpropagates26.666667938232422/Regular400/LH32px/0px. A restores5.333333492279053/Bold700/LH160.0000023841858%/tracking−2%;localinstanceIDremains empty.'),
('restoration','Count exact restoration and cleanup complete','12checks;independentreads issues[];control/relations/originalguards unchanged;fullinternalArestoredhashesequal. CLEANUP_COMPLETE. Hugegeometry/propertyrowsomittedfromtransport only;fullinternalcomparisonsretained.')],
13:[
('coverage','Exact103 native evidence coverage','PASS103ranges/3pages/242APIroutes/9principaltexts/5components/103emptylocalIDs/0typographicoverrides. Scalegroups14×2/3,76×5/6,13×4/3;3pilots36controls.'),
('chains','Actual API chain and binding verification','Sixrawparts/fingerprints,exactmappingcoverage,nearestinstance/getMainComponentAsync/actualchildrenpath,canonicalprincipalstyleID,exactbindings,effectiverecipe,scale,andallancestorcounterparts. NoIDsuffixreconstruction orancestorscalemultiplication.'),
('slots','Six raw issues and real Options Slot boundary','Retains6COUNTERPART_PATH_MISSING atouter467:1052 indices5/6/7;44routescrosslocalcontent. InstanceI467:1052;456:440 andmain456:440 areAPI SLOT withOptions#466:0. EachinnerCheckboxprovesitsowncanonicalmain;noindexneighboridentity.'),
('tests','Eight inheritance evidence regression tests','PASSrealcoverage plusrejectionwrongmain,typooverride,FramecalledSlot,newinstancebinding,wrongprincipalbindingidentity,emptyprincipalstyleID,missingtransportpart.'),
('overlay','Evidence proof and final acceptance separation','Proofdoesnotmodifycontracts. Finaloverlaymustjoincurrent34censuses,3250directranges/150editorials,QA79 andexplicitnormativeactivation;historicalmapping/checkerremainintact.')],
14:[
('visual','Three native clarification cards inspected','Cards1006:672/677/682 completelegibletitles,samples,metrics,IDs,descriptions;norecrop/overlap. Eachgrows22pxAutoLayout. TinyCount remainsboundedcompatibilityexception.'),
('preservation','Description-only card operation preservation','79currentstyles+1historical=80recipesunchanged;3styledescriptions+11documentationtextschanged;3cards+8referencesreadback,0overflows. Notconsumerproof.'),
('prefix','Final two usage-prefix clarifications','Small2/3→DropdownItemSmall;Medium5/6→DropdownItemMedium+Select. Finalreadback/QA/screenspassed;metrics/samples/dimensionsunchanged;previousimagesretained;Countunchanged.')],
15:[
('cards','Four new underline specimens','4cardsPASSvisual,16newtextscheckedforboxes/styleIDs,75previouscardspreserved. Underlinevisible/textlegible/nocropinoverlap;doesnotvalidatecomponentconsumption.')],
16:[
('provisional','Historical provisional graph inventory','Plan2007sources:140new24changed0deleted,65semantic(62docs3PNG),99code/datachanged.1843eligibleunchanged(912semantic931code);notexecutedcachehits. Historicalbaseline1867sources11592nodes27352edges.'),
('retry','Bounded real large-JSON retry','EightJSON>1MiB≤8MiBatcut;retryonlyactualsizefailuresusingoriginalextractorpatchedinmemory,keepfailedAST/report,requiredataJSONclassificationandstructuralsupplement. Neveremptyfailed_sourcesfabrication.'),
('sequence','Planned graph freeze and publish gates','Finalsource/releasefreeze→docs/status→uniqueprepare/backups→AST+fullsemantics→actualJSONretry/supplement→stagingclose+hashes+integrity→smokequeries/CURRENT. Noexecutionsclaimedbyplan.')],
17:[
('scope','Proposed bounded native substitution','Proposalonly:REQ/AC-TYP-004,TYC-01/06,13groups Select64/Dropdown26/Header12/AppShell1. Need103realchains+threecausalfactors+finalindependentreadbackbeforeadoption;only5/6pilotcompleteatthiscut.'),
('binding','Proposed metric identity and binding separation','JoinpageId/nodeId/start/end;INHERITED_NATIVE_SCALE,metricStyleLogicalId/recipeScale1,principalstyle+nodeID,nativescale,actualinstancechain,observedemptylocalID,evidence. No fakeID/doublescale/suffixreconstruction.'),
('catalog','Proposed documentary catalog0.1.2','79metrics/IDs/bindings/units/decoration/factorspreserved. Only3descriptions+3reasons+encodingexplanation+version/provenancechange;no80thstyleorhistoricalrewrite.'),
('closure','Proposed downstream closure','Fourregistryfamiliesgainnewamendment;webregenerationpreserves79recipes;skillsretainmaterializedlogicalIDandnativeevidence;patchrelease0.2.1afterQA;rootgraphcloseafterfreeze. Allproposalstatesremainhistorical.')],
18:[
('candidate','Provisional candidate test scope','1927DSsources43families;catalog0.1.1;Next/TypeScriptPASS;14/14offline10instances5families23sources124fragments;HTML3741588bytes. Threevisualsamplesonly.'),
('limits','Provisional candidate is not final release','Notpublished,current0.2.0,repoMatchFalse,ds_digest20460f38d63226d54224a121828a7556dde772ea85436be3c2e9776d4f7e543b. FigmaNOT_RUN/103scaledBLOCKED;futurefreezenotproved.'),
('retries','Provisional rejected attempts retained','Concurrentregistrychangeinvalidatedfirstcut;firstChromesandboxlaunchNOT_RUNpreserved,authorizedisolatedretryPASS. No sourcefailurehidden.')],
19:[
('preflight','Historical immutable release preconditions','Rootfreeze required,current0.2.0/version0.2.1absent,changedfingerprintmatchestestedcandidate. sync--bumppatch;CLIhasno--version. Stoponmismatch;neveroverwritehistory.'),
('offline','Planned portable candidate acceptance','14states/viewports10instances,movedrenamedisolatedfile://,conditionalassets,Enter/Escape/edit;zeroHTTP/errors/brokenimages/unmappedtext;MDselfcontainedJSON+hashes. Fivefixturefamiliesnotall43norFigma.'),
('install','Managed install preserves user edits','Afterexactmanifestcompare/reexportUNCHANGED,authorizedmanagedinstallandcheck-installed. Rejectpreserveeditedcopies;oldskillsintact. No Figma orGraphwritesinplan.'),
('archive','Intact portable handoff archive','PreserveHTML/MD/captures/dependencieswithrelativepaths. NeverarchiveisolatedMDwhoseassetfoldersaremissing;duplicatesnapshotomissionrequiresdigestrecovery.')],
20:[
('measurements','Web79-class and43-family measured scope','PASS316classmeasurements(79×4themes),2956consumermeasurements;realManrope,identity,weight,size,LH,tracking,decorationchecked. NoFigmaevidence.'),
('preservation','Web75→79 preservation','2956measurementsretainmetrics/text/classification;0metricdifferences;48webthemevariantidentitieschangedto4underlineIDs. Do notconfuse48webobservationswith27Figmaranges.'),
('checks','Web generator build and browser checks','11PythontestsPASS,determinism/typecheck/buildPASS,2browser testsPASS. Initialsandboxlocalhostfailurebeforeassertionsretained;authorizedretrycompleted.'),
('visual','Three Personas web visual samples','ButtonLink/FileUpload/EmptyStatesreviewed:expectedunderlinelegibleandnorecropinmuestras. Notallframepositions/allcompositions/pixelidentity. Sourcehistorical103Figmablockremainsseparate.')],
21:[
('release','Final paired release0.2.1 identity','CURRENTpackages/install;2131sources43families79stylesactive0.1.2. DSdigest4205fc48bf65ef7f42f3c51f15402d61c7f5e25ae88850f1a50ccd41fb90bc67;input14696426ec4dc9591a40d0b9fd7a925ad54b570c7f925bcd51a5a1424783ff39. Synccreated/exportunchanged.'),
('reproducibility','Re-export and legacy preservation','4300filesbytes+mtimeunchanged;bothZIPCRCPASS;13packaging/installtestsPASS;oldskilltrees1900/462filesandhistoricalZIPsdigestpreserved.'),
('offline','Final standalone file HTML browser proof','PASS14states1440×900/1000×760;Chrome149.0.7827.201;HTML3741671bytesSHA09d2e59e405f6b925cbe9c47159f498762a2046d49c1208be684a26a22783d9e. Movedrenamedfileisolated,nored,0errors/brokenimages/unmappedtext;ModalMedia/SideBySide/close/Enter/Escape/inputtested.'),
('handoff','Self-contained Markdown independent forward proof','24sourceshashverified,10identities,82nodeobservations,124fragments8styles;43amendmentsinpackage. FivefixturefamiliesButton/InputField/Modal/Avatar/Logos;native103notexercisedinthosefamilies,9syntheticregressionsseparate. JSON/MDdifferonlyrepeatedCSSvarmaps.'),
('limits','Final release scope and destination limits','Visualreview2capturesonly,12notmanuallyreviewed;originalhandoffvisualNOT_RUNretained;typographyIDENTIFIEDnotuniversalrecipeconformity;newFigmaNOT_RUN;humanPENDING;Tablelostguardexplicit;graphcurrentnessseparate.'),
('docs','Final release documentary check','PASS1091JSON272frontmatter21historicalfindings4warnings. Self-referentialreportemptyduringreadattemptretained;temporaryoutputretrypassedwithoutcontentchanges.')]
}
for i,rows in D.items():
 for k,label,summary in rows:
  fact(i,k,label,summary=summary,historical=bool(meta[i][1].get('historical',False)))
# Preserve rationale in relevant mechanisms, not extra WHY nodes.
for i,k in [(0,'authority'),(0,'native'),(0,'graph'),(1,'readback'),(2,'portable'),(3,'authority'),(3,'format'),(3,'scale'),(5,'validation'),(9,'criteria'),(9,'ink'),(13,'overlay'),(16,'retry'),(19,'archive')]:
 n=next(n for n in g['nodes'] if n['id']==keys[(i,k)]);n['file_type']='rationale';n['rationale']=n['summary']
styles={};cat=None
for line in Path(files[3]).read_text().splitlines():
 if line.startswith('## Estilos base'):cat='base'
 if line.startswith('## Estilos complementarios'):cat='complementary'
 m=re.search(r'`ds-type-([^`]+)`',line)
 if not m or not line.startswith('| '):continue
 c=[v.strip() for v in line.split('|')[1:-1]]
 if len(c)!=9:continue
 logical=m.group(1);n=node(3,'style_'+logical,c[0],logical_style_id=logical,category=cat,font=c[1],font_size=c[2],line_height=c[3],letter_spacing=c[4],text_decoration=c[5],description=c[6],token_references=c[7].split('<br>'),css_class='ds-type-'+logical,status='DERIVED_REFERENCE_NOT_AUTHORITY');styles[logical]=n;edge(keys[(3,cat)],n,3)
 if logical.endswith('-underline'):edge(n,keys[(3,'format')],3,'implements')
 if 'scaled-' in logical:edge(n,keys[(3,'scale')],3,'implements')
assert len(styles)==79
for logical in ['ui-action-label-medium','ui-action-label-small','ui-action-label-normal','ui-upload-action-feedback']:edge(styles[logical+'-underline'],styles[logical],3,'shares_data_with',detail='Same metrics/bindings; decoration alone differs')
for logical,base in [('ui-checkbox-label-scaled-two-thirds','ui-body-compact'),('ui-checkbox-label-scaled-five-sixths','ui-body-compact'),('micro-count-small-scaled-four-thirds','micro-count-small')]:edge(styles[logical],styles[base],3,'references',detail='Materialized Float32 derivation, no double scale')
assign={}
for m in re.finditer(r'([^{}]+)\{([^{}]*)\}',Path(files[4]).read_text()):
 s=re.search(r'--ds-type-style-id\s*:\s*([a-z0-9-]+)',m.group(2))
 if s:assign.setdefault(s.group(1),[]).append(m.group(1).strip())
for logical,selectors in sorted(assign.items()):
 n=fact(4,'role_'+logical,'Role-based CSS recipe '+logical,'code',logical_style_id=logical,selectors=selectors,mechanism='Shared generated font/tracking recipe plus inspectable identity; role-specific cascade preserves contextual distinctions');assert logical in styles;edge(n,styles[logical],4,'implements')
fact(4,'contextual','Contextual action typography cascade','rationale',rationale='Modal and Empty actions use normal tracking; Empty Link uses normal underline identity. Main Button retains distinct label/text/size recipes.',selectors=['.ds-modal-actions','.ds-empty-actions','.ds-empty-support','.ds-button-link'])
fact(4,'states','Accessible state styling',mechanisms=['focus-visible semantic ring','disabled color/icon/cursor','aria-current/aria-pressed presentation','hidden display none','prefers-reduced-motion disables loader'])
fact(4,'loader','Loader fixed motion cadence',duration_seconds=1.224,hold_ms=1,linear_ms=50,step_degrees=-15,comment='LOADER-001 §8')
fact(4,'selector_geometry','Dropdown selector geometry scale',selector='.ds-option-control',box='24×24',middle_scale='.8333333333',small_scale='.6666666667',limit='Indicator geometry is not proof of scaled Figma text-style linkage')
fact(4,'modal','Modal composition-specific geometry',basic_width=580,small_width=480,large_width=840,side_panels=[500,340],media_height=260,limit='CSS layout, not interaction proof')
# Non-obvious cross-file semantics, with explicit links distinguished from inferences.
relations=[(0,'native',13,'chains'),(0,'skills',21,'release'),(0,'graph',16,'sequence'),(1,'readback',13,'chains'),(2,'portable',21,'offline'),(3,'format',20,'preservation'),(4,'contextual',9,'criteria'),(5,'validation',21,'limits'),(6,'scope',13,'overlay'),(10,'causal',11,'causal'),(11,'causal',12,'causal'),(13,'slots',0,'slots_gate'),(17,'binding',13,'chains'),(17,'scope',6,'scope'),(18,'limits',19,'preflight'),(19,'offline',21,'offline'),(19,'archive',21,'handoff'),(20,'visual',15,'cards')]
for a,k,b,l in relations:edge(keys[(a,k)],keys[(b,l)],a,'semantically_similar_to' if (a,b) in [(10,11),(11,12),(5,21),(20,15)] else 'conceptually_related_to','INFERRED',.85 if (a,b) in [(1,13),(4,9),(11,12),(20,15)] else .95)
for a,k,b,l in [(1,'transforms',9,'counts'),(1,'geometry',9,'geometry'),(2,'typography',3,'api'),(2,'gate',5,'deliverable'),(6,'catalog_diff',8,'catalog'),(8,'coverage',7,'historical_scope'),(8,'limits',7,'table'),(8,'limits',9,'guards'),(8,'native',13,'coverage'),(8,'cleanup',12,'restoration'),(8,'catalog',14,'preservation'),(13,'coverage',10,'causal'),(13,'coverage',11,'causal'),(13,'coverage',12,'causal'),(21,'limits',8,'limits')]:edge(keys[(a,k)],keys[(b,l)],a)
# Only frozen before graph is consulted for previously known artifact endpoints.
oldart={}
for n in old['nodes']:
 if '_artifact_' in n['id']:
  p=Path(n.get('source_file',''));p=p if p.is_absolute() else R/p;oldart[str(p.resolve())]=n['id']
internal={p:roots[i] for i,p in enumerate(files)}
for i,p in enumerate(files):
 if i==4:continue
 for target in re.findall(r'\]\(([^)]+)\)',Path(p).read_text()):
  if '://' in target or target.startswith('#'):continue
  targetpath=str((Path(p).parent/target.split('#')[0]).resolve());tid=internal.get(targetpath) or oldart.get(targetpath)
  if tid and tid!=roots[i]:edge(roots[i],tid,i,'cites')
g['hyperedges']=[
 dict(id=stem(files[13])+'_three_causal_factors',label='Three independently restored scale factors support exact103-chain evidence',nodes=[keys[(10,'causal')],keys[(11,'causal')],keys[(12,'causal')],keys[(13,'coverage')]],relation='form',confidence='EXTRACTED',confidence_score=1.0,source_file=files[13]),
 dict(id=stem(files[9])+'_separate_qa_dimensions',label='Canonical typography, original boxes and literal ink remain separate QA dimensions',nodes=[keys[(9,'criteria')],keys[(9,'guards')],keys[(9,'ink')]],relation='participate_in',confidence='EXTRACTED',confidence_score=1.0,source_file=files[9]),
 dict(id=stem(files[21])+'_paired_delivery',label='Shared release identity, reproducibility, offline execution and portable handoff form paired skill delivery',nodes=[keys[(21,'release')],keys[(21,'reproducibility')],keys[(21,'offline')],keys[(21,'handoff')]],relation='form',confidence='EXTRACTED',confidence_score=1.0,source_file=files[21])]
def validate(data,paths):
 ids={n['id'] for n in data['nodes']};oldids={n['id'] for n in old['nodes']};assert len(ids)==len(data['nodes']);assert len(data['hyperedges'])<=3
 for n in data['nodes']:assert n['source_file'] in paths and re.fullmatch('[a-z0-9_]+',n['id']) and n['file_type'] in ['code','document','paper','image','rationale','concept']
 for e in data['edges']:
  assert e['source'] in ids and e['target'] in ids|oldids;assert e['source_file'] in paths
  assert e['confidence_score']==1.0 if e['confidence']=='EXTRACTED' else e['confidence_score'] in [.95,.85,.75,.65,.55]
 for h in data['hyperedges']:assert len(h['nodes'])>=3 and set(h['nodes'])<=ids and h['source_file'] in paths
 for p in paths:
  expect=plan['source_sha256'].get(p,plan['source_sha256'].get(str(Path(p).relative_to(R))));assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==expect,p
validate(g,files);(run/'chunk-00.json').write_text(json.dumps(g,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'chunk':'00','nodes':len(g['nodes']),'edges':len(g['edges']),'hyperedges':len(g['hyperedges']),'sources':len({n['source_file'] for n in g['nodes']}),'styles':len(styles),'css_recipe_roles':len(assign),'hashes':'PASS'}))
# Vision was completed individually for all four actual PNGs. Printed values are observed text, not measured font or bindings.
vision={
11:('Underline typography specimen: contextual Empty states Link',[
 ('card','Pale rounded specimen card','A light blue-gray rounded panel contains a title, large underlined sample sentence, printed metadata, logical ID and restricted usage paragraph.'),
 ('title','UI/Action/Label Normal/Underline','Printed title at top left.'),
 ('sample','Underlined Spanish sample sentence','Visible bold underlined text: La información clara facilita cada decisión.'),
 ('metadata','Printed Normal Link typography metrics','Visible text says Manrope Bold, Peso700,16px,Interlínea20px,Tracking0px,DecoraciónUNDERLINE. These are printed declarations, not independently measured properties.'),
 ('logical_id','ui-action-label-normal-underline','Printed logical identifier below metrics.'),
 ('restriction','Printed Empty states contextual restriction','Visible paragraph limits underlined Link to Empty states, mentions eight censused ranges and normal tracking, and says not to propagate to main Button or Chat plan names. Printed claims do not verify census or bindings.')]),
12:('Underline typography specimen: File Upload action',[
 ('card','Pale rounded specimen card','A light blue-gray rounded panel contains title, underlined sample, printed metadata, logical ID and usage explanation.'),
 ('title','UI/Upload/Action and feedback/Underline','Printed title at top left.'),
 ('sample','Underlined Spanish sample sentence','Visible semibold underlined text: La información clara facilita cada decisión.'),
 ('metadata','Printed Upload action typography metrics','Visible text says Manrope SemiBold,Peso600,14px,Interlínea20px,Tracking0px,DecoraciónUNDERLINE. Printed declarations, not independently measured properties.'),
 ('logical_id','ui-upload-action-feedback-underline','Printed logical identifier below metrics.'),
 ('restriction','Printed Upload action and feedback distinction','Visible paragraph says action is underlined, four census ranges preserved, success/error feedback stays without underline and shared TextStyle supplies decoration. It does not itself prove those bindings/counts.')]),
13:('Web Button Link visible specimen',[
 ('variant','link/large/default','Small visible variant label at top left.'),
 ('surface','Outlined rounded specimen region','White image with light rounded rectangular sample boundary.'),
 ('label','Underlined Button label','Purple/magenta underlined word Button centered in the sample.'),
 ('left_icon','Left circled plus icon','Purple outlined plus enclosed by circle to the left of Button.'),
 ('right_icon','Right circled plus icon','Matching circled plus to the right of Button.')]),
14:('Web Empty state visible specimen',[
 ('variant','default','Small visible variant label at top left.'),
 ('panel','Large rounded empty-state panel','White panel bounded by a pale rounded outline, with a centered vertical content stack.'),
 ('illustration','Abstract navy and periwinkle illustration','Large rounded-square illustration above text, with dark navy ground and thick periwinkle curved shapes.'),
 ('title','Empty state title','Dark emphasized heading Empty state centered below illustration.'),
 ('description','Description text','Smaller Description centered under title.'),
 ('primary_action','Filled Action button','Purple rounded button labeled Action in white, with circled plus icons on both sides.'),
 ('support','Underlined Support action','Purple underlined Support beneath primary button, with matching circled plus icons on both sides.')])}
for chunk,(title,items) in vision.items():
 paths=json.loads((run/f'chunk-{chunk:02}.files.json').read_text());p=paths[0];v=fresh();rid=stem(p)+'_visual_specimen'
 def vn(k,label,summary):
  ident=stem(p)+'_'+norm(k);v['nodes'].append(dict(id=ident,label=label,file_type='image' if k=='visual_specimen' else 'concept',source_file=p,source_location=None,source_url=None,captured_at=None,author=None,contributor=None,summary=summary,evidence_status='OBSERVED',limits='Visible pixels/printed text only; no measured bindings, font properties, interaction or approval implied'));return ident
 vn('visual_specimen',title,'Actual image visually inspected; extraction records visible composition and text.')
 ids={}
 for k,label,summary in items:
  ids[k]=vn(k,label,summary);v['edges'].append(dict(source=rid,target=ids[k],relation='references',confidence='EXTRACTED',confidence_score=1.0,source_file=p,source_location=None,weight=1.0))
 def ve(a,b,detail):v['edges'].append(dict(source=ids[a],target=ids[b],relation='conceptually_related_to',confidence='EXTRACTED',confidence_score=1.0,source_file=p,source_location=None,weight=1.0,detail=detail))
 if chunk in [11,12]:
  ve('sample','metadata','Printed metadata is positioned below the sample');ve('logical_id','restriction','Identifier and usage paragraph are visibly grouped in the card');hkeys=['title','sample','metadata','logical_id','restriction'];hl='Visible title, sample and printed recipe documentation form a typography specimen'
 elif chunk==13:
  ve('left_icon','label','Circled plus visibly precedes label');ve('right_icon','label','Circled plus visibly follows label');hkeys=['left_icon','label','right_icon'];hl='Paired circled-plus icons frame the underlined action label'
 else:
  ve('illustration','title','Illustration is above the heading');ve('title','description','Description is below heading');ve('primary_action','support','Filled action is above separate underlined Support action');hkeys=['illustration','title','description','primary_action','support'];hl='Centered illustration, explanation and two action treatments form the empty-state hierarchy'
 v['hyperedges']=[dict(id=stem(p)+'_visible_composition',label=hl,nodes=[ids[k] for k in hkeys],relation='form',confidence='EXTRACTED',confidence_score=1.0,source_file=p)]
 validate(v,paths);(run/f'chunk-{chunk:02}.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'chunk':f'{chunk:02}','nodes':len(v['nodes']),'edges':len(v['edges']),'hyperedges':len(v['hyperedges']),'sources':1,'hashes':'PASS'}))
